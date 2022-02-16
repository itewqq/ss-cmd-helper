import argparse
import requests
import base64
import json
import traceback
import subprocess
import psutil

CONFIG = "config.json"
PROCNAME = "sslocal"


def start_proxy(url, port=1089):
    try:
        proc = subprocess.Popen(
            ["sslocal", "-b", "127.0.0.1:%d" % (port), "--server-url", url]
        )
        print("[Start] Success!")
    except Exception:
        print(traceback.format_exc())
    return


def stop_proxy():
    for proc in psutil.process_iter():
        if proc.name() == PROCNAME:
            proc.kill()
            print("[Stop] Success!")
            return
    print("[Stop] Failed, no process named: %s" % (PROCNAME))
    return


def add_subs(url: str):
    try:
        req = requests.get(url=url)
        base64_resp = req.text
        node_list = [
            b.decode() for b in base64.b64decode(base64_resp).strip().split(b"\n")
        ]
        with open(CONFIG, "w") as outfile:
            json.dump({"subs_url": url, "node_list": node_list}, outfile)
        print("[Add] Success! Added %s" % (url))
    except Exception:
        print(traceback.format_exc())

    return


def update():
    try:
        with open(CONFIG, "r+") as outfile:
            config = json.load(outfile)
            req = requests.get(url=config["subs_url"])
            base64_resp = req.text
            node_list = [
                b.decode() for b in base64.b64decode(base64_resp).strip().split(b"\n")
            ]
            config["node_list"] = node_list
            outfile.seek(0)
            json.dump(config, outfile)
            outfile.truncate()
            print("[Update] Success!")
    except Exception:
        print(traceback.format_exc())

    return


def list():
    # TODO: pretify the output
    try:
        with open(CONFIG, "r") as outfile:
            config = json.load(outfile)
            print("Subscription url is: %s\n" % (config["subs_url"]))
            print("Total: %d\n" % (len(config["node_list"])))
            for idx,node in enumerate(config["node_list"]):
                print("[%d]  %s"%(idx, node))
    except Exception:
        print(traceback.format_exc())

    return


def select(idx: int):
    with open(CONFIG, "r+") as outfile:
        config = json.load(outfile)
        config["last_used"] = idx
        outfile.seek(0)
        json.dump(config, outfile)
        outfile.truncate()
        start_proxy(config["node_list"][idx])

    return


def main():
    parser = argparse.ArgumentParser(
        description="Shadowsocks subscription commandline helper."
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-a",
        "--addurl",
        metavar="URL",
        action="store",
        type=str,
        help="add your subsciption URL",
    )
    group.add_argument(
        "-s",
        "--select",
        metavar="n",
        action="store",
        type=int,
        help="select node n to use",
    )
    group.add_argument("-k", "--kill", action="store_true", help="kill sslocal/stop proxy")
    group.add_argument("-u", "--update", action="store_true", help="update subsciption")
    group.add_argument("-l", "--list", action="store_true", help="list all nodes")

    args = parser.parse_args()

    if args.addurl:
        add_subs(args.addurl)
    elif args.select:
        select(args.select)
    elif args.kill:
        stop_proxy()
    elif args.update:
        update()
    elif args.list:
        list()

    return


if __name__ == "__main__":
    main()
