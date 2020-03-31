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
* Tue Mar 31 2020 11:06:15 +0000 Martin Juhl <mj@casalogic.dk> 1.14.1.git843604c-1
- New version build: 1.14.1.git843604c-1
* Mon Mar 30 2020 21:06:03 +0000 Martin Juhl <mj@casalogic.dk> 1.14.1.gitadf4782-1
- New version build: 1.14.1.gitadf4782-1
* Fri Mar 27 2020 17:05:38 +0000 Martin Juhl <mj@casalogic.dk> 1.14.1.git5471088-1
- New version build: 1.14.1.git5471088-1
* Fri Mar 27 2020 08:05:56 +0000 Martin Juhl <mj@casalogic.dk> 1.14.1.gitec60839-1
- New version build: 1.14.1.gitec60839-1
* Thu Mar 26 2020 21:05:45 +0000 Martin Juhl <mj@casalogic.dk> 1.14.1.git255a063-1
- New version build: 1.14.1.git255a063-1
* Wed Mar 25 2020 22:06:03 +0000 Martin Juhl <mj@casalogic.dk> 1.14.1.git93346bc-1
- New version build: 1.14.1.git93346bc-1
* Tue Mar 24 2020 20:06:17 +0000 Martin Juhl <mj@casalogic.dk> 1.14.1.gitccf6ee7-1
- New version build: 1.14.1.gitccf6ee7-1
* Mon Mar 23 2020 00:06:05 +0000 Martin Juhl <mj@casalogic.dk> 1.14.1.git91dd194-1
- New version build: 1.14.1.git91dd194-1
* Sun Mar 22 2020 16:06:23 +0000 Martin Juhl <mj@casalogic.dk> 1.14.1.git7a6a3e4-1
- New version build: 1.14.1.git7a6a3e4-1
* Sat Mar 21 2020 18:01:02 +0000 Martin Juhl <mj@casalogic.dk> 1.14.1.git94341f9-1
- New version build: 1.14.1.git94341f9-1
* Fri Mar 20 2020 10:05:55 +0000 Martin Juhl <mj@casalogic.dk> 1.14.git94341f9-1
- New version build: 1.14.git94341f9-1
* Thu Mar 19 2020 18:06:19 +0000 Martin Juhl <mj@casalogic.dk> 1.14.gitff19fb3-1
- New version build: 1.14.gitff19fb3-1
* Thu Mar 19 2020 13:06:16 +0000 Martin Juhl <mj@casalogic.dk> 1.14.git935f386-1
- New version build: 1.14.git935f386-1
* Wed Mar 18 2020 18:06:29 +0000 Martin Juhl <mj@casalogic.dk> 1.14.gitb85d548-1
- New version build: 1.14.gitb85d548-1
* Mon Mar 16 2020 23:06:09 +0000 Martin Juhl <mj@casalogic.dk> 1.14.gitdce054e-1
- New version build: 1.14.gitdce054e-1
* Mon Mar 16 2020 18:06:07 +0000 Martin Juhl <mj@casalogic.dk> 1.14.git7d9c701-1
- New version build: 1.14.git7d9c701-1
* Sun Mar 15 2020 17:06:19 +0000 Martin Juhl <mj@casalogic.dk> 1.14.git2ee07ea-1
- New version build: 1.14.git2ee07ea-1
* Sat Mar 14 2020 23:05:46 +0000 Martin Juhl <mj@casalogic.dk> 1.14.git40c339d-1
- New version build: 1.14.git40c339d-1
* Sat Mar 14 2020 22:05:08 +0000 Martin Juhl <mj@casalogic.dk> 1.14.gitafd9f4e-1
- New version build: 1.14.gitafd9f4e-1
* Sat Mar 14 2020 15:05:44 +0000 Martin Juhl <mj@casalogic.dk> 1.14.git47a9461-1
- New version build: 1.14.git47a9461-1
* Fri Mar 13 2020 17:01:13 +0000 Martin Juhl <mj@casalogic.dk> 1.14.git70f3ab8-1
- New version build: 1.14.git70f3ab8-1
* Mon Mar 09 2020 22:06:33 +0000 Martin Juhl <mj@casalogic.dk> 1.13.1.git70f3ab8-1
- New version build: 1.13.1.git70f3ab8-1
* Thu Mar 05 2020 00:06:16 +0000 Martin Juhl <mj@casalogic.dk> 1.13.1.git161cccc-1
- New version build: 1.13.1.git161cccc-1
* Tue Mar 03 2020 00:06:16 +0000 Martin Juhl <mj@casalogic.dk> 1.13.1.git1f775f4-1
- New version build: 1.13.1.git1f775f4-1
* Mon Mar 02 2020 19:06:12 +0000 Martin Juhl <mj@casalogic.dk> 1.13.1.git536672a-1
- New version build: 1.13.1.git536672a-1
* Sun Mar 01 2020 14:05:56 +0000 Martin Juhl <mj@casalogic.dk> 1.13.1.git2ebff95-1
- New version build: 1.13.1.git2ebff95-1
* Sun Mar 01 2020 02:05:57 +0000 Martin Juhl <mj@casalogic.dk> 1.13.1.gitedfdda8-1
- New version build: 1.13.1.gitedfdda8-1
* Sun Feb 23 2020 14:06:00 +0000 Martin Juhl <mj@casalogic.dk> 1.13.1.gitcd89075-1
- New version build: 1.13.1.gitcd89075-1
* Sat Feb 22 2020 22:06:24 +0000 Martin Juhl <mj@casalogic.dk> 1.13.1.git8a5450e-1
- New version build: 1.13.1.git8a5450e-1
* Tue Feb 18 2020 21:05:32 +0000 Martin Juhl <mj@casalogic.dk> 1.13.1.git63459c5-1
- New version build: 1.13.1.git63459c5-1
* Tue Feb 18 2020 20:06:06 +0000 Martin Juhl <mj@casalogic.dk> 1.13.1.git916e96b-1
- New version build: 1.13.1.git916e96b-1
* Mon Feb 17 2020 23:05:56 +0000 Martin Juhl <mj@casalogic.dk> 1.13.1.git325039c-1
- New version build: 1.13.1.git325039c-1
* Sun Feb 16 2020 22:06:03 +0000 Martin Juhl <mj@casalogic.dk> 1.13.1.gitc5b97f4-1
- New version build: 1.13.1.gitc5b97f4-1
* Tue Feb 04 2020 22:06:41 +0000 Martin Juhl <mj@casalogic.dk> 1.13.1.git8867626-1
- New version build: 1.13.1.git8867626-1
* Thu Jan 30 2020 22:08:52 +0000 Martin Juhl <mj@casalogic.dk> 1.13.1.gitf5916ec-1
- New version build: 1.13.1.gitf5916ec-1
* Wed Jan 29 2020 13:06:43 +0000 Martin Juhl <mj@casalogic.dk> 1.13.1.git5352321-1
- New version build: 1.13.1.git5352321-1
* Tue Jan 28 2020 20:06:48 +0000 Martin Juhl <mj@casalogic.dk> 1.13.1.git632d552-1
- New version build: 1.13.1.git632d552-1
* Sun Jan 26 2020 16:06:57 +0000 Martin Juhl <mj@casalogic.dk> 1.13.1.gitff7b4a3-1
- New version build: 1.13.1.gitff7b4a3-1
* Mon Jan 20 2020 22:06:22 +0000 Martin Juhl <mj@casalogic.dk> 1.13.1.gitd212dfe-1
- New version build: 1.13.1.gitd212dfe-1
* Sun Jan 19 2020 23:06:50 +0000 Martin Juhl <mj@casalogic.dk> 1.13.1.git84ed185-1
- New version build: 1.13.1.git84ed185-1
* Thu Jan 16 2020 16:08:44 +0000 Martin Juhl <mj@casalogic.dk> 1.13.1.gitc0ba340-1
- New version build: 1.13.1.gitc0ba340-1
* Fri Jan 10 2020 18:06:26 +0000 Martin Juhl <mj@casalogic.dk> 1.13.1.git9ebca99-1
- New version build: 1.13.1.git9ebca99-1
* Sun Jan 05 2020 22:05:57 +0000 Martin Juhl <mj@casalogic.dk> 1.13.1.gitbaf7d1b-1
- New version build: 1.13.1.gitbaf7d1b-1
* Sun Jan 05 2020 18:01:07 +0000 Martin Juhl <mj@casalogic.dk> 1.13.1.git59e50b0-1
- New version build: 1.13.1.git59e50b0-1
* Sun Jan 05 2020 17:06:15 +0000 Martin Juhl <mj@casalogic.dk> 1.13.0.git59e50b0-1
- New version build: 1.13.0.git59e50b0-1
* Sun Jan 05 2020 00:06:29 +0000 Martin Juhl <mj@casalogic.dk> 1.13.0.gitc058a1d-1
- New version build: 1.13.0.gitc058a1d-1
* Sat Jan 04 2020 23:06:23 +0000 Martin Juhl <mj@casalogic.dk> 1.13.0.git8c22992-1
- New version build: 1.13.0.git8c22992-1
* Tue Dec 31 2019 02:06:18 +0000 Martin Juhl <mj@casalogic.dk> 1.13.0.git95dd1cd-1
- New version build: 1.13.0.git95dd1cd-1
* Sun Dec 29 2019 15:06:14 +0000 Martin Juhl <mj@casalogic.dk> 1.13.0.git36ae946-1
- New version build: 1.13.0.git36ae946-1
* Sat Dec 28 2019 15:06:19 +0000 Martin Juhl <mj@casalogic.dk> 1.13.0.git8ee0c57-1
- New version build: 1.13.0.git8ee0c57-1
* Fri Dec 27 2019 22:05:57 +0000 Martin Juhl <mj@casalogic.dk> 1.13.0.git5c6081c-1
- New version build: 1.13.0.git5c6081c-1
* Fri Dec 27 2019 18:06:24 +0000 Martin Juhl <mj@casalogic.dk> 1.13.0.git88c56de-1
- New version build: 1.13.0.git88c56de-1
* Sun Dec 22 2019 21:08:03 +0000 Martin Juhl <mj@casalogic.dk> 1.13.0.git4cec502-1
- New version build: 1.13.0.git4cec502-1
* Thu Dec 19 2019 00:06:22 +0000 Martin Juhl <mj@casalogic.dk> 1.13.0.git2545469-1
- New version build: 1.13.0.git2545469-1
* Sun Dec 15 2019 15:07:35 +0000 Martin Juhl <mj@casalogic.dk> 1.13.0.gitf09996a-1
- New version build: 1.13.0.gitf09996a-1
* Sat Dec 07 2019 14:05:48 +0000 Martin Juhl <mj@casalogic.dk> 1.13.0.git5cabf4d-1
- New version build: 1.13.0.git5cabf4d-1
* Fri Dec 06 2019 22:06:15 +0000 Martin Juhl <mj@casalogic.dk> 1.13.0.gita03db6d-1
- New version build: 1.13.0.gita03db6d-1
* Tue Dec 03 2019 00:08:31 +0000 Martin Juhl <mj@casalogic.dk> 1.13.0.gite777be3-1
- New version build: 1.13.0.gite777be3-1
* Sun Dec 01 2019 21:06:01 +0000 Martin Juhl <mj@casalogic.dk> 1.13.0.gitadc443e-1
- New version build: 1.13.0.gitadc443e-1
* Sat Nov 30 2019 23:05:44 +0000 Martin Juhl <mj@casalogic.dk> 1.13.0.gitb45b02b-1
- New version build: 1.13.0.gitb45b02b-1
* Sat Nov 30 2019 15:01:00 +0000 Martin Juhl <mj@casalogic.dk> 1.13.0.git1e22422-1
- New version build: 1.13.0.git1e22422-1
* Thu Nov 28 2019 22:05:43 +0000 Martin Juhl <mj@casalogic.dk> 1.12.0.git1e22422-1
- New version build: 1.12.0.git1e22422-1
* Wed Nov 27 2019 21:06:28 +0000 Martin Juhl <mj@casalogic.dk> 1.12.0.git3471e26-1
- New version build: 1.12.0.git3471e26-1
* Mon Nov 25 2019 08:05:48 +0000 Martin Juhl <mj@casalogic.dk> 1.12.0.git924ba15-1
- New version build: 1.12.0.git924ba15-1
* Sun Nov 24 2019 18:06:02 +0000 Martin Juhl <mj@casalogic.dk> 1.12.0.gitcf5a985-1
- New version build: 1.12.0.gitcf5a985-1
* Sat Nov 23 2019 16:06:20 +0000 Martin Juhl <mj@casalogic.dk> 1.12.0.git486c7d8-1
- New version build: 1.12.0.git486c7d8-1
* Fri Nov 22 2019 15:05:47 +0000 Martin Juhl <mj@casalogic.dk> 1.12.0.git4b71197-1
- New version build: 1.12.0.git4b71197-1
* Wed Nov 20 2019 19:01:09 +0000 Martin Juhl <mj@casalogic.dk> 1.12.0.gitcbadf00-1
- New version build: 1.12.0.gitcbadf00-1
* Tue Nov 19 2019 20:07:33 +0000 Martin Juhl <mj@casalogic.dk> 1.11.0.gitcbadf00-1
- New version build: 1.11.0.gitcbadf00-1
* Sat Nov 16 2019 23:06:01 +0000 Martin Juhl <mj@casalogic.dk> 1.11.0.gitc5b7447-1
- New version build: 1.11.0.gitc5b7447-1
* Fri Nov 15 2019 00:06:01 +0000 Martin Juhl <mj@casalogic.dk> 1.11.0.gita19a6fb-1
- New version build: 1.11.0.gita19a6fb-1
* Wed Nov 13 2019 22:07:45 +0000 Martin Juhl <mj@casalogic.dk> 1.11.0.gitcd83a9e-1
- New version build: 1.11.0.gitcd83a9e-1
* Mon Nov 11 2019 18:05:58 +0000 Martin Juhl <mj@casalogic.dk> 1.11.0.gitf563871-1
- New version build: 1.11.0.gitf563871-1
* Thu Nov 07 2019 20:05:55 +0000 Martin Juhl <mj@casalogic.dk> 1.11.0.git3f39e35-1
- New version build: 1.11.0.git3f39e35-1
* Wed Nov 06 2019 21:06:12 +0000 Martin Juhl <mj@casalogic.dk> 1.11.0.git9ff577a-1
- New version build: 1.11.0.git9ff577a-1
* Tue Nov 05 2019 18:05:44 +0000 Martin Juhl <mj@casalogic.dk> 1.11.0.git07e0fdb-1
- New version build: 1.11.0.git07e0fdb-1
* Mon Nov 04 2019 14:06:23 +0000 Martin Juhl <mj@casalogic.dk> 1.11.0.git9a0fe6f-1
- New version build: 1.11.0.git9a0fe6f-1
* Sat Nov 02 2019 18:05:22 +0000 Martin Juhl <mj@casalogic.dk> 1.11.0.gite449912-1
- New version build: 1.11.0.gite449912-1
* Sat Nov 02 2019 17:05:48 +0000 Martin Juhl <mj@casalogic.dk> 1.11.0.git72a46fb-1
- New version build: 1.11.0.git72a46fb-1
* Sat Nov 02 2019 00:05:51 +0000 Martin Juhl <mj@casalogic.dk> 1.11.0.gite2e3712-1
- New version build: 1.11.0.gite2e3712-1
* Tue Oct 29 2019 15:05:48 +0000 Martin Juhl <mj@casalogic.dk> 1.11.0.git77b78f0-1
- New version build: 1.11.0.git77b78f0-1
* Fri Oct 25 2019 23:05:56 +0000 Martin Juhl <mj@casalogic.dk> 1.11.0.git97d41c2-1
- New version build: 1.11.0.git97d41c2-1
* Fri Oct 25 2019 20:11:49 +0000 Martin Juhl <mj@casalogic.dk> 1.11.0.gitfccc0a4-1
- New version build: 1.11.0.gitfccc0a4-1
* Thu Oct 17 2019 19:09:47 +0000 Martin Juhl <mj@casalogic.dk> 1.11.0.git95a7ffd-1
- New version build: 1.11.0.git95a7ffd-1
* Wed Oct 16 2019 18:11:18 +0000 Martin Juhl <mj@casalogic.dk> 1.11.0.gitcd8acc2-1
- New version build: 1.11.0.gitcd8acc2-1
* Tue Oct 15 2019 21:13:01 +0000 Martin Juhl <mj@casalogic.dk> 1.11.0.gitd3054d4-1
- New version build: 1.11.0.gitd3054d4-1
* Mon Oct 14 2019 00:05:58 +0000 Martin Juhl <mj@casalogic.dk> 1.11.0.git7d956c5-1
- New version build: 1.11.0.git7d956c5-1
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
