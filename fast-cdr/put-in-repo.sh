#!/bin/bash
ssh repo.rpm mkdir -p /var/www/html/repos/ros/Packages
scp rpmbuild/RPMS/x86_64/* repo.rpm:/var/www/html/repos/ros/Packages/
ssh repo.rpm createrepo --update /var/www/html/repos/
