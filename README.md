# gowikicharm

## Description

This charm installs a simple go web server that allows you to create, edit and view pages.

## Usage

- Make sure you have the following tools installed and setup juju (2.9.29), microk8s, charmcraft (1.6.0).
- Build the Charm using charmcraft 
  - `cd gowikicharm && charmcraft pack`
- Bootstrap your environment on microk8s `juju bootstrap microk8s micro`
- Add your model to the controller `juju add-model development`
- In one terminal run `juju debug-log`, in another run `watch -n1 --color juju status --color`
- Deploy the charm locally `juju deploy ./gowikicharm_ubuntu-20.04-amd64.charm --resource gowiki-image=mrparish/gowiki`
- if the charm was deployed successfully you should have output similar to the one below.
```
Every 1.0s: juju status --color                                         evanson: Thu May 12 10:59:48 2022

Model        Controller  Cloud/Region        Version  SLA          Timestamp
development  micro       microk8s/localhost  2.9.29   unsupported  10:59:49+03:00

App          Version  Status  Scale  Charm        Channel  Rev  Address         Exposed  Message
gowikicharm           active      1  gowikicharm             1  10.152.183.118  no

Unit            Workload  Agent  Address     Ports  Message
gowikicharm/0*  active    idle   10.1.87.94
```

## Relations

TODO: Provide any relations which are provided or required by your charm

## OCI Images

https://index.docker.io/v1/

## Contributing

Please see the [Juju SDK docs](https://juju.is/docs/sdk) for guidelines
on enhancements to this charm following best practice guidelines, and
`CONTRIBUTING.md` for developer guidance.
