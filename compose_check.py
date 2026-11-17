from pathlib import Path
import yaml

def check_document(document):
    issues=[]
    if not isinstance(document,dict):
        return ["top-level YAML value must be a mapping"]
    services=document.get("services")
    if not isinstance(services,dict) or not services:
        return ["'services' must be a non-empty mapping"]
    host_ports={}
    names=set(services)
    for name,config in services.items():
        if not isinstance(config,dict):
            issues.append(f"service '{name}' must be a mapping")
            continue
        if not config.get("image") and not config.get("build"):
            issues.append(f"service '{name}' needs either 'image' or 'build'")
        depends=config.get("depends_on",[])
        deps=depends.keys() if isinstance(depends,dict) else depends
        if not isinstance(deps,(list,tuple,dict_keys_type())):
            issues.append(f"service '{name}' has an invalid depends_on value")
        else:
            for dep in deps:
                if dep not in names:
                    issues.append(f"service '{name}' depends_on unknown service '{dep}'")
        ports=config.get("ports",[])
        if not isinstance(ports,list):
            issues.append(f"service '{name}' ports must be a list")
            continue
        for entry in ports:
            if isinstance(entry,dict):
                published=entry.get("published")
                host=str(published) if published is not None else None
            elif isinstance(entry,str):
                parts=entry.split("/")[0].split(":")
                host=parts[-2] if len(parts)>=2 else None
                if host and "-" in host: host=host.split("-",1)[0]
            else:
                host=None
            if host and host.isdigit():
                if host in host_ports:
                    issues.append(f"host port {host} is used by both '{host_ports[host]}' and '{name}'")
                else:
                    host_ports[host]=name
    return issues

def dict_keys_type():
    return type({}.keys())

def check_file(path:Path):
    try:
        document=yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError,UnicodeError) as exc:
        return [f"cannot read file: {exc}"]
    except yaml.YAMLError as exc:
        mark=getattr(exc,"problem_mark",None)
        location=f"line {mark.line+1}: " if mark else ""
        return [location+str(exc).splitlines()[0]]
    return check_document(document)
