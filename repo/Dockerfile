#TODO: https://linuxthegreat.wordpress.com/2017/03/05/creating-custom-yum-repo/
#TODO: get scp working; uploading seems to require custom module
#TODO: https://blog.packagecloud.io/eng/2014/11/24/howto-gpg-sign-verify-rpm-packages-yum-repositories/
#TODO: https://docs.nginx.com/nginx/admin-guide/security-controls/
#TODO: https://www.cyberciti.biz/tips/linux-unix-bsd-nginx-webserver-security.html
#TODO: https://geekflare.com/nginx-webserver-security-hardening-guide/
#TODO: https://www.owasp.org/index.php/SCG_WS_nginx
#TODO: https://dev-sec.io/baselines/nginx/
FROM registry.hub.docker.com/library/centos:centos7

ENV container=docker 

RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7 \
    && yum -y update \
    && yum -y install epel-release -y \
    && rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7 \ 
    && yum -y install createrepo \
         nginx \
         openssh-clients \
         openssh-server \
         supervisor \
         yum-utils
COPY ssh /
RUN mv id_rsa /etc/ssh/ssh_host_rsa_key \
    && mv id_rsa.pub /etc/ssh/host_rsa_key.pub \
    && ssh-keygen -f /etc/ssh/ssh_host_dsa_key -N '' -t dsa \
    && mkdir -p /var/www/html/repos/
COPY files /
RUN groupadd rpm_uploaders \
    && chmod +x /root/addusers.sh \
    && /root/addusers.sh \
    && chown -R root:rpm_uploaders /var/www/html/repos/ \
    && chmod 775 /var/www/html/repos/
CMD ["supervisord","-n"]
