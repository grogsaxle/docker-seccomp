A little docker demo for secconf

    $ docker built -t test
    $ docker run --rm -it --security-opt seccomp=${PWD}/profiles/seccomp_centos_default.json test
    $ docker run --rm -it --security-opt seccomp=${PWD}/profiles/seccomp_centos_no_uname.json test

With uname in seccomp profile
    $ docker run -it --security-opt seccomp=profiles/seccomp_centos_default.json ubuntu bash
    root@14ea56c3d20b:/# exit


No uname in seccomp profile
    $ docker run -it --security-opt seccomp=profiles/seccomp_centos_no_uname.json ubuntu bash
    root@??host??:/# exit


