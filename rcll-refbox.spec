%global commit d403548448a7a4cf450a034d70f807ff94aefdfd
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:		  rcll-refbox
Version:	2021
Release:	0.2.%{shortcommit}%{?dist}
Summary:	The referee box (refbox) of the RoboCup Logistics League

License:	GPLv2+
URL:		  https://github.com/robocup-logistics/rcll-refbox
Source0:  https://github.com/robocup-logistics/rcll-refbox/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires: apr-util-devel
BuildRequires: avahi-devel
BuildRequires: boost-devel
BuildRequires: clips-devel
BuildRequires: clipsmm-devel
BuildRequires: freeopcua-devel
BuildRequires: gcc-c++
BuildRequires: gecode-devel
BuildRequires: git
BuildRequires: glibmm24-devel
BuildRequires: gtkmm30-devel
BuildRequires: libmicrohttpd-devel
BuildRequires: mongo-cxx-driver-devel
BuildRequires: ncurses-devel
BuildRequires: openssh-clients
BuildRequires: openssl-devel
BuildRequires: protobuf-compiler
BuildRequires: protobuf-devel
BuildRequires: rapidjson-devel
BuildRequires: which
BuildRequires: yaml-cpp-devel

%description
%{summary}.


%prep
%autosetup -p1 -n %{name}-%{commit}


%build
CFLAGS="%{optflags}"
export CFLAGS
make switch-buildtype-sysinstall
make %{?_smp_mflags} \
  FAIL_ON_WARNING=1 \
  EXEC_CONFDIR=%{_sysconfdir}/rcll-refbox/ \
  EXEC_BINDIR=%{_bindir} \
  EXEC_LIBDIR=%{_libdir} \
  EXEC_SHAREDIR=%{_datadir}/rcll-refbox \
  uncolored-all


%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_libdir}
mkdir -p %{buildroot}/%{_datadir}/rcll-refbox/{games,msgs}
mkdir -p %{buildroot}/%{_sysconfdir}/rcll-refbox/cfg

find ./bin \( -name "llsf*" -o -name "rcll*" \) -exec install -p '{}' %{buildroot}/%{_bindir}/ \;
find ./lib -type f -exec install -p '{}' %{buildroot}/%{_libdir}/ \;
cp -a ./src/games/* %{buildroot}/%{_datadir}/rcll-refbox/games
install -p ./src/msgs/*.proto %{buildroot}/%{_datadir}/rcll-refbox/msgs
# TODO: This should be installed in RESDIR and should be handled by make install.
mkdir -p %{buildroot}/%{_datadir}/rcll-refbox/libs/websocket/message_schemas
install -p ./src/libs/websocket/message_schemas/*.json %{buildroot}/%{_datadir}/rcll-refbox/libs/websocket/message_schemas
cp -a ./cfg/* %{buildroot}/%{_sysconfdir}/rcll-refbox/

%files
%doc
%{_bindir}/*
%{_libdir}/*
%{_datadir}/rcll-refbox
%{_sysconfdir}/rcll-refbox


%changelog
* Sat Nov  14 15:29:55 CET 2021 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - 2021-0.2.f9fe119
- Update to customizable configuration loading

* Fri May  14 09:33:51 CET 2021 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - 2021-0.1.b9d0129
- Update to latest upstream commit

* Thu Dec  3 13:18:55 CET 2020 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 2020-0.9.4a64ed0
- Install websocket message schemas

* Thu Dec  3 08:07:53 CET 2020 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 2020-0.8.4a64ed0
- Update to latest upstream commit
- Add patch to fix compiler warnings on Fedora 33

* Mon Nov  9 16:36:49 CET 2020 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 2020-0.7.ec52966
- Update to latest upstream commit

* Mon May 04 2020 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 2020-0.6.cdd5a2f
- Update to latest upstream commit

* Tue Apr 28 2020 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 2020-0.5.d3d554b
- Update to latest upstream commit

* Thu Apr 23 2020 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 2020-0.4.4799979
- Rebuild for soname change in freeopcua

* Sat Mar 21 2020 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 2020-0.3.4799979
- Update to latest upstream commit
- Re-enable avahi
- Enable FAIL_ON_WARNING

* Fri Mar 20 2020 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 2020-0.2.1544b29
- Disable AVAHI

* Mon Mar 16 2020 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 2020-0.1.1544b29
- Update to 2020 pre-release snapshot

* Sun Oct 13 2019 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 2019-2.848b440
- Switch to git snapshots, update to latest commit

* Thu Sep 12 2019 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 2019-1
- Update to latest release 2019

* Sun Jun 23 2019 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 2019~beta.2-3
- Rebuild without mongodb support

* Sun Jun 23 2019 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 2019~beta.2-2
- Also install protobuf message libraries

* Sun Jun 23 2019 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 2019~beta.2-1
- Initial package
