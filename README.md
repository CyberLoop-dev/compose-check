<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:101827,100:%2338bdf8&height=170&section=header&text=Compose%20Check&fontSize=40&fontColor=ffffff" alt="Compose Check banner"/></p>
<p align="center"><img src="https://readme-typing-svg.demolab.com?font=Inter&weight=600&size=22&pause=1000&color=38bdf8&center=true&vCenter=true&width=650&lines=Catch%20Docker%20Compose%20mistakes%20before%20startup" alt="Typing title"/></p>
<p align="center"><img src="https://img.shields.io/github/license/CyberLoop-dev/compose-check"/> <img src="https://img.shields.io/github/languages/top/CyberLoop-dev/compose-check"/> <img src="https://img.shields.io/github/stars/CyberLoop-dev/compose-check"/> <img src="https://img.shields.io/github/last-commit/CyberLoop-dev/compose-check"/></p>
<p align="center"><img src="assets/overview.svg" alt="Compose Check illustration" width="92%"/></p>

## 🧭 Overview
Compose Check performs a small static review of a local Docker Compose file. It validates service definitions, dependency references, and obvious host-port collisions without starting containers.

## ✨ Features
- 🧩 Checks that services have an image or build configuration.
- 🔗 Finds depends_on references to missing services.
- 🚦 Detects repeated numeric host-port bindings.
- 🛡️ Reads configuration only; it never invokes Docker.

## 🎬 Demo
```text
$ python main.py compose.yaml
compose.yaml: services.api: depends_on references unknown service 'cache'
compose.yaml: host port 8080 is used by both 'web' and 'api'
2 issue(s) found.
```
This is a local example, not a hosted demo.

## 🚀 Quick Start
```bash
python -m pip install -r requirements.txt
python main.py examples/compose.yaml
```
The checker intentionally covers a practical subset of Compose syntax. It does not replace `docker compose config`.

## 🧰 Tech Stack
- Python 3.10+
- PyYAML safe loading
- unittest

## 🗂️ Folder Structure
```text
main.py
compose_check.py
tests/test_compose_check.py
examples/compose.yaml
assets/overview.svg
requirements.txt
```

## 🗺️ Roadmap
- [x] Core local workflow
- [x] Documented command-line or browser interface
- [ ] Broader edge-case coverage
- [ ] Optional CI examples

## 🤝 Contributing
Issues and focused pull requests are welcome. Add regression tests for bug fixes and document new options.

## 📄 License
Released under the [MIT License](LICENSE).

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:101827,100:%2338bdf8&height=110&section=footer" alt="Animated footer"/></p>
