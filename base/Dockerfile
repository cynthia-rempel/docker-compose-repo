FROM registry.hub.docker.com/library/centos:centos7

ENV container=docker

# base image
RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7 \
    && yum -y update \
    && yum -y install epel-release -y \
    && rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7 \
    && yum -y install \
       bzip2 \
       cmake3 \
       gcc-c++ \
       make \
       mock \
       openssh-clients \
       rpm-build \
       rpmdevtools \
       wget \
       yum-utils \
    && wget https://getfedora.org/static/9DB62FB1.txt \
    && cat 9DB62FB1.txt > /etc/pki/rpm-gpg/RPM-GPG-KEY-FEDORA28 \
    && rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-FEDORA28
#    && useradd base \
#    && usermod -a -G mock base
# COPY ssh/ /home/base/.ssh
# RUN chown -R base:base /home/base/.ssh
# USER base
# RUN rpmdev-setuptree
