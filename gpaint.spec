%define	name	gpaint-2
%define	version	0.3.3
%define release %mkrel 2 

Name:		%{name}
Summary:	Simple, easy-to-use paint program
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Source0:	http://alpha.gnu.org/gnu/gpaint/%{name}-%{version}.tar.gz
URL:		http://www.gnu.org/software/gpaint/
Group:		Graphics
Patch0:		gpaint-2-0.3.3-fix-drawing-fnt.patch
Patch1:		gpaint-2-0.3.3-fix-rebuild.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libglade2.0-devel >= 2.6.4

%description
GNU Paint. A simple, easy-to-use paint program for GNOME. This is a port of
xpaint that takes advantages of features unique to the GNOME environment.

%prep
%setup -q
%patch0 -p1 
%patch1 -p0

%build
%configure2_5x 
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
%find_lang %{name}

#mdk menu entry
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Gpaint
Comment=Paint program
Exec=%{_bindir}/%{name}
Icon=graphics_section
Terminal=false
Type=Application
Categories=Graphics;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root root) 
%doc AUTHORS COPYING  NEWS README THANKS
%{_bindir}/%{name}
%{_datadir}/gpaint/glade/gpaint.glade
%{_datadir}/applications/%{name}.desktop

