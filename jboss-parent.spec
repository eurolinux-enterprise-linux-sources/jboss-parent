Name:                 jboss-parent
Version:              6
Release:              11%{?dist}
Summary:              JBoss Parent POM
Group:                Development/Libraries
License:              LGPLv2+
URL:                  http://www.jboss.org/

# git clone git://github.com/jboss/jboss-parent-pom.git
# cd jboss-parent-pom/ && git archive --format=tar --prefix=jboss-parent-6/ 6 | xz > jboss-parent-6.tar.xz
Source0:              %{name}-%{version}.tar.xz
# Removing unavailable deps
Patch0:               %{name}-%{version}-deps.patch
BuildArch:            noarch

BuildRequires:        jpackage-utils
BuildRequires:        maven-local
BuildRequires:        maven-install-plugin
BuildRequires:        maven-javadoc-plugin
BuildRequires:        maven-release-plugin
BuildRequires:        maven-resources-plugin
BuildRequires:        maven-enforcer-plugin


%description
The Project Object Model files for JBoss packages.

%prep
%setup -q
%patch0 -p1

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md

%changelog
* Mon Aug 26 2013 Michal Srb <msrb@redhat.com> - 6-11
- Migrate away from mvn-rpmbuild (Resolves: #997506)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 6-9
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 19 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 6-7
- Simplify requires since they are only in depManagement

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 12 2011 Alexander Kurtakov <akurtako@redhat.com> 6-5
- Add missing BR.

* Tue Sep 20 2011 Marek Goldmann <mgoldman@redhat.com> 6-4
- Removed unavailable deps from POM

* Mon Aug 29 2011 Marek Goldmann <mgoldman@redhat.com> 6-3
- Added maven-surefire-provider-junit requires

* Thu Jul 28 2011 Marek Goldmann <mgoldman@redhat.com> 6-2
- Added build section
- Removed unnecessary sections and BR's

* Mon Jul 18 2011 Marek Goldmann <mgoldman@redhat.com> 6-1
- Upstream release: 6.

* Tue Jun 07 2011 Marek Goldmann <mgoldman@redhat.com> 6-0.1.beta2
- Initial packaging
