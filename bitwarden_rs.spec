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
%attr(0755, bitwarden, bitwarden) %{service_homedir}/server/bin/bitwarden_rs
%attr(0644, root, root) %{_unitdir}/bitwarden_rs.service

%changelog
* Sat Oct 12 2019 15:04:56 +0000 Martin Juhl <mj@casalogic.dk> 1.11.0.gitdc515b8-1
- New version build: 1.11.0.gitdc515b8-1
* Fri Oct 11 2019 21:09:58 +0000 Martin Juhl <mj@casalogic.dk> 1.11.0.gitd3bd277-1
- New version build: 1.11.0.gitd3bd277-1
* Fri Oct 11 2019 14:05:23 +0000 Martin Juhl <mj@casalogic.dk> 1.11.0.gitf482585-1
- New version build: 1.11.0.gitf482585-1
* Thu Oct 10 2019 22:05:42 +0000 Martin Juhl <mj@casalogic.dk> 1.11.0.gitd292269-1
- New version build: 1.11.0.gitd292269-1
* Thu Oct 10 2019 00:06:21 +0000 Martin Juhl <mj@casalogic.dk> 1.11.0.git0586c00-1
- New version build: 1.11.0.git0586c00-1
* Tue Oct 08 2019 23:05:18 +0000 Martin Juhl <mj@casalogic.dk> 1.11.0.git45d9d8d-1
- New version build: 1.11.0.git45d9d8d-1
* Tue Oct 08 2019 18:09:01 +0000 Martin Juhl <mj@casalogic.dk> 1.11.0.git881c197-1
- New version build: 1.11.0.git881c197-1
* Tue Oct 08 2019 17:05:19 +0000 Martin Juhl <mj@casalogic.dk> 1.10.0.gitb4b62c2-1
- New version build: 1.10.0.gitb4b62c2-1
* Sat Oct 05 2019 16:04:51 +0000 Martin Juhl <mj@casalogic.dk> 1.10.0.git99a635d-1
- New version build: 1.10.0.git99a635d-1
* Sat Oct 05 2019 15:05:56 +0000 Martin Juhl <mj@casalogic.dk> 1.10.0.gitc182583-1
- New version build: 1.10.0.gitc182583-1
* Tue Oct 01 2019 18:06:30 +0000 Martin Juhl <mj@casalogic.dk> 1.10.0.gite7b8602-1
- New version build: 1.10.0.gite7b8602-1
* Wed Sep 11 2019 21:05:46 +0000 Martin Juhl <mj@casalogic.dk> 1.10.0.gitf9408a0-1
- New version build: 1.10.0.gitf9408a0-1
* Sat Sep 07 2019 21:05:36 +0000 Martin Juhl <mj@casalogic.dk> 1.10.0.gitae8bf95-1
- New version build: 1.10.0.gitae8bf95-1
* Fri Sep 06 2019 09:05:21 +0000 Martin Juhl <mj@casalogic.dk> 1.10.0.gitc656f2f-1
- New version build: 1.10.0.gitc656f2f-1
* Thu Sep 05 2019 20:08:19 +0000 Martin Juhl <mj@casalogic.dk> 1.10.0.gitdf8114f-1
- New version build: 1.10.0.gitdf8114f-1
* Thu Sep 05 2019 18:07:06 +0000 Martin Juhl <mj@casalogic.dk> 1.10.0.gitdda244e-1
- New version build: 1.10.0.gitdda244e-1
* Tue Sep 03 2019 19:05:38 +0000 Martin Juhl <mj@casalogic.dk> 1.10.0.git65c0d10-1
- New version build: 1.10.0.git65c0d10-1
* Sat Aug 31 2019 16:07:41 +0000 Martin Juhl <mj@casalogic.dk> 1.10.0.git7dcf181-1
- New version build: 1.10.0.git7dcf181-1
* Wed Aug 28 2019 11:22:47 +0000 Martin Juhl <mj@casalogic.dk> 1.10.0.git469318b-1
- New version build: 1.10.0.git469318b-1
* Tue Aug 27 2019 20:12:57 +0000 Martin Juhl <mj@casalogic.dk> 1.9.1.git469318b-1
- New version build: 1.9.1.git469318b-1
* Tue Aug 27 2019 19:05:41 +0000 Martin Juhl <mj@casalogic.dk> 1.9.1.git2c2276c-1
- New version build: 1.9.1.git2c2276c-1
* Wed Aug 21 2019 16:05:30 +0000 Martin Juhl <mj@casalogic.dk> 1.9.1.git026f9da-1
- New version build: 1.9.1.git026f9da-1
* Tue Aug 20 2019 22:06:02 +0000 Martin Juhl <mj@casalogic.dk> 1.9.1.gitd23d4f2-1
- New version build: 1.9.1.gitd23d4f2-1
* Tue Aug 20 2019 19:06:11 +0000 Martin Juhl <mj@casalogic.dk> 1.9.1.git515b877-1
- New version build: 1.9.1.git515b877-1
* Mon Aug 19 2019 21:07:02 +0000 Martin Juhl <mj@casalogic.dk> 1.9.1.gitd8ea3d2-1
- New version build: 1.9.1.gitd8ea3d2-1
* Sun Aug 18 2019 19:01:49 +0000 Martin Juhl <mj@casalogic.dk> 1.9.1.git07743e4-1
* Sun Aug 18 2019 18:20:20 +0000 Martin Juhl <mj@casalogic.dk> 1.9.1.git07743e4-1
- New version build: 1.9.1.git07743e4-1
* Thu Aug 15 2019 21:05:43 +0000 Martin Juhl <mj@casalogic.dk> 1.9.1.git27c23b6-1
- New version build: 1.9.1.git27c23b6-1
* Tue Jul 30 2019 18:12:12 +0000 Martin Juhl <mj@casalogic.dk> 1.9.1.git8be2ed6-1
- New version build: 1.9.1.git8be2ed6-1
* Thu Jul 18 2019 09:39:30 +0000 Martin Juhl <mj@casalogic.dk> 1.9.1.git05a1137-6
- New version build: 1.9.1.git05a1137-6
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
