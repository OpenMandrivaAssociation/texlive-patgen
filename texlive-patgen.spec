# revision 29764
# category TLCore
# catalog-ctan /obsolete/systems/knuth/unsupported/texware/patgen.web
# catalog-date 2012-06-09 20:15:34 +0200
# catalog-license knuth
# catalog-version 2.3
Name:		texlive-patgen
Epoch:		1
Version:	2.3
Release:	2
Summary:	Generate hyphenation patterns
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/obsolete/systems/knuth/unsupported/texware/patgen.web
License:	KNUTH
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/patgen.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/patgen.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
