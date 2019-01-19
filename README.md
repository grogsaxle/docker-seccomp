A little docker demo for secconf

    $ docker built -t test
    $ docker run --rm -it --security-opt seccomp=${PWD}/profiles/seccomp_centos_default.json test
    $ docker run --rm -it --security-opt seccomp=${PWD}/profiles/seccomp_centos_no_uname.json test

