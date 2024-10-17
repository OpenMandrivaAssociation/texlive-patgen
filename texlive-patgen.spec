Name:		texlive-patgen
Epoch:		1
Version:	70015
Release:	1
Summary:	Generate hyphenation patterns
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/obsolete/systems/knuth/unsupported/texware/patgen.web
License:	KNUTH
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/patgen.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/patgen.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-kpathsea
Requires:	texlive-patgen.bin

%description
This is the last version of the program distributed by Knuth;
it advertises itself as a pattern generator for "the algorithm
used in TeX", but, of course, the patterns used in modern
distributions are Unicode-based.

#-----------------------------------------------------------------------
%files
%doc %{_mandir}/man1/patgen.1*
%doc %{_texmfdistdir}/doc/man/man1/patgen.man1.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
