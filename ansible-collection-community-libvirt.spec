Name:           ansible-collection-community-libvirt
Version:        1.0.2
Release:        1.VERS%{?dist}
Summary:        None
License:        UNKNOWN
URL:            https://github.com/ansible-collections/community.libvirt
Source0:        https://galaxy.ansible.com/download/ansible-collection-community-libvirt-%{version}.tar.gz
BuildArch:      noarch

Requires:       ansible


%description
None

%prep
%autosetup -c ansible-collection-community-libvirt-%{version}-%{release}

%build


%install
rm -rf tests
install -d -m 0755 %{buildroot}/%{_datadir}/ansible/collections/ansible_collections/community/libvirt/
cp -rp * %{buildroot}/%{_datadir}/ansible/collections/ansible_collections/community/libvirt/

%files
%license COPYING
%doc README.md
%{_datadir}/ansible/collections/ansible_collections/community/libvirt/


%changelog

* Thu Apr 21 2022 Bill Peck <bpeck@redhat.com> - 1.0.2-1
- Initial package
