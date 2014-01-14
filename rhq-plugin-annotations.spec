%{?_javapackages_macros:%_javapackages_macros}
Name:             rhq-plugin-annotations
Version:          3.0.4
Release:          6.0%{?dist}
Summary:          RHQ plugin annotations

License:          GPL and LGPLv2+
URL:              http://rhq-project.org

# git clone git://git.fedorahosted.org/rhq/rhq.git
# git checkout rhq-pluginGen-3.0.4
# cd rhq/modules/helpers/
# tar cafJ rhq-plugin-annotations-3.0.4.tar.xz pluginAnnotations
Source0:          rhq-plugin-annotations-%{version}.tar.xz
Patch0:           rhq-plugin-annotations-%{version}-pom.patch

BuildArch:        noarch

BuildRequires:    java-devel
BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin

Requires:         java
Requires:         jpackage-utils

%description
Annotations to help generate RHQ plugin descriptors

%package javadoc
Summary:          Javadocs for %{name}

Requires:         jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n pluginAnnotations
%patch0 -p1

%build
mvn-rpmbuild -Dproject.build.sourceEncoding=iso8859-1  install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 target/rhq-pluginAnnotations-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 3.0.4-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 6 2012 Ricardo Arguello <ricardo@fedoraproject.org> 3.0.4-2
- Cleanup of the spec file

* Mon Nov 21 2011 Marek Goldmann <mgoldman@redhat.com> 3.0.4-1
- Initial packaging
