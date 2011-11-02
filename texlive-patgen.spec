Name:		texlive-patgen
Version:	20111102
Release:	1
Summary:	TeXLive patgen package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/patgen.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/patgen.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-kpathsea
Requires:	texlive-patgen.bin
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
TeXLive patgen package.

#-----------------------------------------------------------------------
%files
%doc %{_mandir}/man1/patgen.1*
%doc %{_texmfdir}/doc/man/man1/patgen.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
