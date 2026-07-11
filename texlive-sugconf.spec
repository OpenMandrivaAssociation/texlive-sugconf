%global tl_name sugconf
%global tl_revision 58752

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	SAS(R) user group conference proceedings document class
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/conferences/sugconf
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sugconf.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sugconf.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class may be used to typeset articles to be published in the
proceedings of SAS(R) User group conferences and workshops. The layout
produced by the class is based on that published by SAS Institute
(2021).

