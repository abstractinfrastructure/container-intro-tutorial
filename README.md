# Introduction to Container Tutorial

## Before you Begin

These exercises accompany the presentation [Introduction to Containers]. To
participate in the labs, install the [Docker Community Edition (CE) Engine][ce].
**NOTE:** For linux users, you will need to additionally install
[docker-compose].


- [OSX Install](https://docs.docker.com/docker-for-mac/install/)
- [Windows Install](https://docs.docker.com/docker-for-windows/install/)
- Linux Distro Specific Install
  - [CentOS](https://docs.docker.com/install/linux/docker-ce/centos/)
  - [Debian](https://docs.docker.com/install/linux/docker-ce/debian/)
  - [Fedora](https://docs.docker.com/install/linux/docker-ce/fedora/)
  - [Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

To verify that you have docker installed and working correct. Execute the
following:
```bash
docker run hello-world
```

If you see a message similar to the following text, Docker is installed and
working.
```bash
Hello from Docker!
This message shows that your installation appears to be working correctly.
...
```

If you failed to see the above message, check these resources for
troubleshooting:

- [Troubleshooting OSX Install](https://docs.docker.com/docker-for-mac/troubleshoot/)
- [Troubleshooting Windows Install](https://docs.docker.com/docker-for-windows/troubleshoot/)

---

## Exercise Index

- [Lifecycle]
- [Images]
- [Networking]
- [Storage]
- [Inspecting and Debugging]
- [Developer Workflow]
- [Best Practices, Security, and Tips]


[Introduction to Containers]: https://docs.google.com/presentation/d/1P7TlA2TF4xRWMyVcjC7WQTRdQE3O7R1CJII5UPfHt2s/edit?usp=sharing
[ce]: https://docs.docker.com/install/
[docker-compse]: https://docs.docker.com/compose/install/
[lifecycle]: /lifecycle/README.md
[images]: /images/README.md
[networking]: /networking/README.md
[storage]: /storage/README.md
[inspecting and debugging]: /inspecting-and-debugging/README.md
[developer workflow]: /developer-workflow/README.md
[Best Practices, Security, and Tips]: /best-practices-and-tips