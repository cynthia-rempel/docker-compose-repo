NAME: nexus
Version: 3.15.2
Release: 01
Summary: Manage components, and build artifacts in one central location
License: NEXUS OSS
URL: https://www.sonatype.com/nexus-repository-oss
Source0: https://github.com/sonatype/nexus-public/archive/release-%{version}-%{release}.tar.gz
BuildArch: noarch
BuildRequires: epel-release
BuildRequires: centos-release-scl
BuildRequires: createrepo
BuildRequires: rh-maven35
BuildRequires: rh-maven35-ant-javamail
BuildRequires: rh-maven35-aopalliance
BuildRequires: rh-maven35-apache-commons-beanutils
BuildRequires: rh-maven35-apache-commons-cli
BuildRequires: rh-maven35-apache-commons-codec
BuildRequires: rh-maven35-apache-commons-collections
BuildRequires: rh-maven35-apache-commons-digester
BuildRequires: rh-maven35-apache-commons-io
BuildRequires: rh-maven35-apache-commons-jexl
BuildRequires: rh-maven35-apache-commons-lang
BuildRequires: rh-maven35-apache-commons-lang3
BuildRequires: rh-maven35-apache-commons-validator
BuildRequires: rh-maven35-cdi-api
BuildRequires: rh-maven35-glassfish-jaxb-api
BuildRequires: rh-maven35-glassfish-servlet-api
BuildRequires: rh-maven35-guava
BuildRequires: rh-maven35-glassfish-annotation-api
BuildRequires: rh-maven35-guice-assistedinject
BuildRequires: rh-maven35-guice
BuildRequires: rh-maven35-guice-assistedinject
BuildRequires: rh-maven35-guice-servlet
BuildRequires: rh-maven35-jackson-annotations
BuildRequires: rh-maven35-jakarta-commons-httpclient
BuildRequires: rh-maven35-javapackages-local
BuildRequires: rh-maven35-javapackages-tools
BuildRequires: rh-maven35-jline
BuildRequires: rh-maven35-joda-time
BuildRequires: rh-maven35-junit
BuildRequires: rh-maven35-maven-artifact
BuildRequires: rh-maven35-maven-local
BuildRequires: rh-maven35-maven-enforcer
BuildRequires: rh-maven35-maven-enforcer-api
BuildRequires: rh-maven35-maven-enforcer-plugin
BuildRequires: rh-maven35-maven-enforcer-rules
BuildRequires: rh-maven35-jackson-annotations
BuildRequires: rh-maven35-jackson-core
BuildRequires: rh-maven35-jackson-annotations
BuildRequires: rh-maven35-jsr-305
BuildRequires: rh-maven35-osgi-core
BuildRequires: rh-maven35-plexus-classworlds
BuildRequires: rh-maven35-plexus-interpolation
BuildRequires: rh-maven35-python-javapackages
BuildRequires: rh-maven35-plexus-utils
BuildRequires: rh-maven35-slf4j
BuildRequires: rh-maven35-sisu-inject
BuildRequires: rh-maven35-snakeyaml
BuildRequires: rh-maven35-velocity
BuildRequires: rh-maven35-xz-java
BuildRequires: unzip


%description
Manage components, and build artifacts in one central location

# %package        javadoc
# Summary:        Javadoc for %{name}
# %description javadoc
# This package contains the API documentation for %{name}.

%prep

%setup -n nexus-public-release-%{version}-%{release}

%build

cd buildsupport
# speed up the build by caching artifacts
/opt/rh/rh-maven35/root/usr/bin/mvn -T 20C dependency:go-offline -Dmaven.repo.local=%{_builddir}/repository install -Denforcer.skip=true -Dmaven.test.skip=true
cd ..
/opt/rh/rh-maven35/root/usr/bin/mvn -T 20C dependency:go-offline -Dmaven.repo.local=%{_builddir}/repository install -Denforcer.skip=true -Dmaven.test.skip=true

%install
mkdir -p %{buildroot}/opt
unzip %{_builddir}/nexus-public-release-%{version}-%{release}/assemblies/nexus-base-template/target/nexus-base-template-%{version}-%{release}.zip \
      -d %{buildroot}/opt/
%files
/*

%changelog

