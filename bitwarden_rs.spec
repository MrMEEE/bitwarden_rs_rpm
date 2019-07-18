%define  debug_package %{nil}
%global __os_install_post %{nil}

%define service_user bitwarden
%define service_group bitwarden
%define service_homedir /opt/bitwarden_rs
%define service_logdir /var/log/bitwarden_rs
%define service_configdir /etc/bitwarden_rs

Summary: Bitwarden RS
Name: bitwarden_rs
Version: ¤VERSION¤
Release: ¤BUILDRELEASE¤%{dist}
Source0: bitwarden_rs-¤RELEASE¤
Source1: bitwarden_rs.service
Source2: bitwarden_rs.conf-¤RELEASE¤
License: GPLv3
Group: System Tools
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}.buildroot
AutoReqProv: false
Requires: bitwarden_rs_web

%description
%{summary}

%prep

%install
mkdir -p $RPM_BUILD_ROOT%{service_homedir}/server/bin
mkdir -p $RPM_BUILD_ROOT%{service_configdir}
mkdir -p $RPM_BUILD_ROOT%{service_homedir}/server/data
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
mkdir -p %{buildroot}%{service_logdir}
mkdir -p %{buildroot}%{service_configdir}

install -m 755 %{SOURCE0} %{buildroot}/%{service_homedir}/server/bin/bitwarden_rs
install -m 755 %{SOURCE1} %{buildroot}/%{_unitdir}/bitwarden_rs.service
install -m 755 %{SOURCE2} %{buildroot}/%{service_configdir}/bitwarden-rs.conf


%pre
/usr/bin/getent group %{service_group} >/dev/null || /usr/sbin/groupadd --system %{service_group}
/usr/bin/getent passwd %{service_user} >/dev/null || /usr/sbin/useradd --no-create-home --system -g %{service_group} --home-dir %{service_homedir} -s /bin/bash %{service_user}
/usr/sbin/usermod -s /bin/bash %{service_user}

%post
%systemd_post bitwarden_rs

%preun
%systemd_preun bitwarden_rs

%postun
%systemd_postun bitwarden_rs

%clean

%files
%defattr(0644, bitwarden, bitwarden, 0755)
%config %{service_configdir}/bitwarden-rs.conf
%{service_homedir}/server
%dir %{service_homedir}/server/data
%attr(0755, bitwarden, bitwarden) %{buildroot}/%{service_homedir}/server/bin/bitwarden_rs
%attr(0644, root, root) %{_unitdir}/bitwarden_rs.service

%changelog
* Wed Jul 17 2019 20:02:08 +0000 Martin Juhl <mj@casalogic.dk> 1.9.1.git05a1137
* Wed Jul 17 2019 19:45:00 +0000 Martin Juhl <mj@casalogic.dk> 1.9.1.git05a1137
* Wed Jul 17 2019 12:58:58 +0000 Martin Juhl <mj@casalogic.dk> 1.9.1.git05a1137
- New version build: 1.9.1.git05a1137
* Tue Jul 16 2019 22:40:50 +0000 Martin Juhl <mj@casalogic.dk> 05a1137
* Tue Jul 16 2019 22:39:33 +0000 Martin Juhl <mj@casalogic.dk> 05a1137
* Tue Jul 16 2019 22:37:49 +0000 Martin Juhl <mj@casalogic.dk> 05a1137
* Tue Jul 16 2019 22:34:01 +0000 Martin Juhl <mj@casalogic.dk> 05a1137
* Tue Jul 16 2019 22:25:46 +0000 Martin Juhl <mj@casalogic.dk> 05a1137
- New version build: 05a1137
