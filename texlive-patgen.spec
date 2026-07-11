%global tl_name patgen
%global tl_revision 77830

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.4
Release:	%{tl_revision}.1
Summary:	Generate hyphenation patterns
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/systems/stanford/patgen
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/patgen.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/patgen.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(kpathsea)
Requires:	texlive(patgen.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Patgen takes a list of hyphenated words and generates a set of patterns
that can be used by the TeX 82 hyphenation algorithm. Patgen was
originally written by Frank M. Liang as part of his Stanford Ph.D. work,
and has always been distributed alongside the other programs coming from
the Stanford TeX project. It was updated in 1991 by Peter Breitenlohner
for the new 8-bit features of TeX version 3. (These updates related to
input/output and programming overhead; the actual pattern generation
algorithms were not changed.) Patgen is currently maintained as part of
TeX Live.

