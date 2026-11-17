import argparse, json
from pathlib import Path
from compose_check import check_file

def main():
    parser=argparse.ArgumentParser(description="Statically check a Docker Compose YAML file.")
    parser.add_argument("file",type=Path)
    parser.add_argument("--json",action="store_true")
    args=parser.parse_args()
    issues=check_file(args.file)
    if args.json: print(json.dumps(issues,indent=2))
    else:
        for issue in issues: print(f"{args.file}: {issue}")
        print(f"{len(issues)} issue(s) found.")
    return 1 if issues else 0

if __name__=="__main__": raise SystemExit(main())
