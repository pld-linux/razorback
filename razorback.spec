Summary:	An intrusion detection tool for GNOME
Summary(pl):	Narzêdzie do wykrywania intruzów dla ¶rodowska GNOME
Name:		razorback
Version:	1.0.3
Release:	1
License:	GPL
Group:		Networking
Source0:	http://www.intersectalliance.com/razorback/%{name}-%{version}.tar.gz
# Source0-md5:	aeb7a76963a4cc753ab264b333ebbcac
URL:		http://www.intersectalliance.com/
BuildRequires:	gtk+-devel
BuildRequires:	gnome-libs-devel
Requires:	gtk+ >= 1.2.7
Requires:	gnome-libs >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Razorback is a monitoring interface to the SNORT intrusion detection
toolkit for GNOME.

%description -l pl
Razorback jest interfejsem dla pakietu SNORT, przeznaczonym dla
¶rodowiska GNOME.

%prep

%setup -q

%build
rm config.cache
%configure2_13
%{__make} \
	   CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir} \
	   $RPM_BUILD_ROOT%{_applnkdir}/Network/Misc \
	   $RPM_BUILD_ROOT%{_pixmapsdir}

install razorback.desktop $RPM_BUILD_ROOT%{_applnkdir}/Network/Misc
install pixmaps/razorback_icon.png $RPM_BUILD_ROOT%{_pixmapsdir}/razorback.png

install src/razorback $RPM_BUILD_ROOT%{_bindir}

%files
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS TODO
%attr(755,root,root) %{_bindir}/razorback
%{_applnkdir}/Network/Misc/*
%{_pixmapsdir}/*

%clean
rm -r $RPM_BUILD_ROOT
