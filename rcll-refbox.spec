%global   nextrel 2019
%global   prerel  beta.2
Name:		  rcll-refbox
Version:	%{nextrel}~%{prerel}
Release:	2%{?dist}
Summary:	The referee box (refbox) of the RoboCup Logistics League

License:	GPLv2+
URL:		  https://github.com/robocup-logistics/rcll-refbox
Source0:	https://github.com/robocup-logistics/rcll-refbox/archive/%{nextrel}-%{prerel}/%{name}-%{nextrel}-%{prerel}.tar.gz
Patch0:   rcll-refbox.uninitialized-machine-light.patch

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
BuildRequires: mongodb-devel
BuildRequires: ncurses-devel
BuildRequires: openssh-clients
BuildRequires: openssl-devel
BuildRequires: protobuf-compiler
BuildRequires: protobuf-devel
BuildRequires: which
BuildRequires: yaml-cpp-devel

%description
%{summary}.


%prep
%autosetup -p1 -n %{name}-%{nextrel}-%{prerel}


%build
CFLAGS="%{optflags}"
export CFLAGS
make switch-buildtype-sysinstall
make %{?_smp_mflags} \
  FAIL_ON_WARNING=1 \
  EXEC_CONFDIR=%{_sysconfdir}/rcll-refbox \
  EXEC_BINDIR=%{_bindir} \
  EXEC_LIBDIR=%{_libdir} \
  EXEC_SHAREDIR=%{_datadir}/rcll-refbox \
  uncolored-all


%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_libdir}
mkdir -p %{buildroot}/%{_datadir}/rcll-refbox/{games,msgs}
mkdir -p %{buildroot}/%{_sysconfdir}/rcll-refbox

install -p ./bin/* %{buildroot}/%{_bindir}/
find ./lib -type f -exec install -p '{}' %{buildroot}/%{_libdir}/ \;
cp -a ./src/games/* %{buildroot}/%{_datadir}/rcll-refbox/games
install -p ./src/msgs/*.proto %{buildroot}/%{_datadir}/rcll-refbox/msgs
install -p ./cfg/* %{buildroot}/%{_sysconfdir}/rcll-refbox


%files
%doc
%{_bindir}/*
%{_libdir}/*
%{_datadir}/rcll-refbox
%{_sysconfdir}/rcll-refbox


%changelog
* Sun Jun 23 2019 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 2019~beta.2-2
- Also install protobuf message libraries

* Sun Jun 23 2019 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 2019~beta.2-1
- Initial package
