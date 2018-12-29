#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : compat-protobuf-soname14
Version  : 3.4.1
Release  : 12
URL      : https://github.com/google/protobuf/archive/v3.4.1.tar.gz
Source0  : https://github.com/google/protobuf/archive/v3.4.1.tar.gz
Summary  : Google's Data Interchange Format
Group    : Development/Tools
License  : BSD-3-Clause
Requires: compat-protobuf-soname14-bin
Requires: compat-protobuf-soname14-python3
Requires: compat-protobuf-soname14-lib
Requires: compat-protobuf-soname14-python
Requires: setuptools
Requires: six
BuildRequires : cmake
BuildRequires : emacs
BuildRequires : go
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : zlib-dev

%description
This is the 'v2' C++ implementation for python proto2.
It is active when:
PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=cpp
PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION_VERSION=2

%package bin
Summary: bin components for the compat-protobuf-soname14 package.
Group: Binaries

%description bin
bin components for the compat-protobuf-soname14 package.


%package dev
Summary: dev components for the compat-protobuf-soname14 package.
Group: Development
Requires: compat-protobuf-soname14-lib
Requires: compat-protobuf-soname14-bin
Provides: compat-protobuf-soname14-devel

%description dev
dev components for the compat-protobuf-soname14 package.


%package lib
Summary: lib components for the compat-protobuf-soname14 package.
Group: Libraries

%description lib
lib components for the compat-protobuf-soname14 package.


%package python
Summary: python components for the compat-protobuf-soname14 package.
Group: Default
Requires: compat-protobuf-soname14-python3

%description python
python components for the compat-protobuf-soname14 package.


%package python3
Summary: python3 components for the compat-protobuf-soname14 package.
Group: Default
Requires: python3-core

%description python3
python3 components for the compat-protobuf-soname14 package.


%prep
%setup -q -n protobuf-3.4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1522675054
%reconfigure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1522675054
rm -rf %{buildroot}
%make_install
## make_install_append content
pushd python
python ./setup.py install --root=%{buildroot}
python3 ./setup.py install --root=%{buildroot}
popd
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/protoc

%files dev
%defattr(-,root,root,-)
%exclude /usr/include/google/protobuf/any.h
%exclude /usr/include/google/protobuf/any.pb.h
%exclude /usr/include/google/protobuf/any.proto
%exclude /usr/include/google/protobuf/api.pb.h
%exclude /usr/include/google/protobuf/api.proto
%exclude /usr/include/google/protobuf/arena.h
%exclude /usr/include/google/protobuf/arena_impl.h
%exclude /usr/include/google/protobuf/arenastring.h
%exclude /usr/include/google/protobuf/compiler/code_generator.h
%exclude /usr/include/google/protobuf/compiler/command_line_interface.h
%exclude /usr/include/google/protobuf/compiler/cpp/cpp_generator.h
%exclude /usr/include/google/protobuf/compiler/csharp/csharp_generator.h
%exclude /usr/include/google/protobuf/compiler/csharp/csharp_names.h
%exclude /usr/include/google/protobuf/compiler/importer.h
%exclude /usr/include/google/protobuf/compiler/java/java_generator.h
%exclude /usr/include/google/protobuf/compiler/java/java_names.h
%exclude /usr/include/google/protobuf/compiler/javanano/javanano_generator.h
%exclude /usr/include/google/protobuf/compiler/js/js_generator.h
%exclude /usr/include/google/protobuf/compiler/js/well_known_types_embed.h
%exclude /usr/include/google/protobuf/compiler/objectivec/objectivec_generator.h
%exclude /usr/include/google/protobuf/compiler/objectivec/objectivec_helpers.h
%exclude /usr/include/google/protobuf/compiler/parser.h
%exclude /usr/include/google/protobuf/compiler/php/php_generator.h
%exclude /usr/include/google/protobuf/compiler/plugin.h
%exclude /usr/include/google/protobuf/compiler/plugin.pb.h
%exclude /usr/include/google/protobuf/compiler/plugin.proto
%exclude /usr/include/google/protobuf/compiler/python/python_generator.h
%exclude /usr/include/google/protobuf/compiler/ruby/ruby_generator.h
%exclude /usr/include/google/protobuf/descriptor.h
%exclude /usr/include/google/protobuf/descriptor.pb.h
%exclude /usr/include/google/protobuf/descriptor.proto
%exclude /usr/include/google/protobuf/descriptor_database.h
%exclude /usr/include/google/protobuf/duration.pb.h
%exclude /usr/include/google/protobuf/duration.proto
%exclude /usr/include/google/protobuf/dynamic_message.h
%exclude /usr/include/google/protobuf/empty.pb.h
%exclude /usr/include/google/protobuf/empty.proto
%exclude /usr/include/google/protobuf/extension_set.h
%exclude /usr/include/google/protobuf/field_mask.pb.h
%exclude /usr/include/google/protobuf/field_mask.proto
%exclude /usr/include/google/protobuf/generated_enum_reflection.h
%exclude /usr/include/google/protobuf/generated_enum_util.h
%exclude /usr/include/google/protobuf/generated_message_reflection.h
%exclude /usr/include/google/protobuf/generated_message_table_driven.h
%exclude /usr/include/google/protobuf/generated_message_util.h
%exclude /usr/include/google/protobuf/has_bits.h
%exclude /usr/include/google/protobuf/io/coded_stream.h
%exclude /usr/include/google/protobuf/io/gzip_stream.h
%exclude /usr/include/google/protobuf/io/printer.h
%exclude /usr/include/google/protobuf/io/strtod.h
%exclude /usr/include/google/protobuf/io/tokenizer.h
%exclude /usr/include/google/protobuf/io/zero_copy_stream.h
%exclude /usr/include/google/protobuf/io/zero_copy_stream_impl.h
%exclude /usr/include/google/protobuf/io/zero_copy_stream_impl_lite.h
%exclude /usr/include/google/protobuf/map.h
%exclude /usr/include/google/protobuf/map_entry.h
%exclude /usr/include/google/protobuf/map_entry_lite.h
%exclude /usr/include/google/protobuf/map_field.h
%exclude /usr/include/google/protobuf/map_field_inl.h
%exclude /usr/include/google/protobuf/map_field_lite.h
%exclude /usr/include/google/protobuf/map_type_handler.h
%exclude /usr/include/google/protobuf/message.h
%exclude /usr/include/google/protobuf/message_lite.h
%exclude /usr/include/google/protobuf/metadata.h
%exclude /usr/include/google/protobuf/metadata_lite.h
%exclude /usr/include/google/protobuf/reflection.h
%exclude /usr/include/google/protobuf/reflection_ops.h
%exclude /usr/include/google/protobuf/repeated_field.h
%exclude /usr/include/google/protobuf/service.h
%exclude /usr/include/google/protobuf/source_context.pb.h
%exclude /usr/include/google/protobuf/source_context.proto
%exclude /usr/include/google/protobuf/struct.pb.h
%exclude /usr/include/google/protobuf/struct.proto
%exclude /usr/include/google/protobuf/stubs/atomic_sequence_num.h
%exclude /usr/include/google/protobuf/stubs/atomicops.h
%exclude /usr/include/google/protobuf/stubs/atomicops_internals_arm64_gcc.h
%exclude /usr/include/google/protobuf/stubs/atomicops_internals_arm_gcc.h
%exclude /usr/include/google/protobuf/stubs/atomicops_internals_arm_qnx.h
%exclude /usr/include/google/protobuf/stubs/atomicops_internals_atomicword_compat.h
%exclude /usr/include/google/protobuf/stubs/atomicops_internals_generic_c11_atomic.h
%exclude /usr/include/google/protobuf/stubs/atomicops_internals_generic_gcc.h
%exclude /usr/include/google/protobuf/stubs/atomicops_internals_mips_gcc.h
%exclude /usr/include/google/protobuf/stubs/atomicops_internals_power.h
%exclude /usr/include/google/protobuf/stubs/atomicops_internals_ppc_gcc.h
%exclude /usr/include/google/protobuf/stubs/atomicops_internals_solaris.h
%exclude /usr/include/google/protobuf/stubs/atomicops_internals_tsan.h
%exclude /usr/include/google/protobuf/stubs/atomicops_internals_x86_gcc.h
%exclude /usr/include/google/protobuf/stubs/atomicops_internals_x86_msvc.h
%exclude /usr/include/google/protobuf/stubs/bytestream.h
%exclude /usr/include/google/protobuf/stubs/callback.h
%exclude /usr/include/google/protobuf/stubs/casts.h
%exclude /usr/include/google/protobuf/stubs/common.h
%exclude /usr/include/google/protobuf/stubs/fastmem.h
%exclude /usr/include/google/protobuf/stubs/hash.h
%exclude /usr/include/google/protobuf/stubs/logging.h
%exclude /usr/include/google/protobuf/stubs/macros.h
%exclude /usr/include/google/protobuf/stubs/mutex.h
%exclude /usr/include/google/protobuf/stubs/once.h
%exclude /usr/include/google/protobuf/stubs/platform_macros.h
%exclude /usr/include/google/protobuf/stubs/port.h
%exclude /usr/include/google/protobuf/stubs/scoped_ptr.h
%exclude /usr/include/google/protobuf/stubs/shared_ptr.h
%exclude /usr/include/google/protobuf/stubs/singleton.h
%exclude /usr/include/google/protobuf/stubs/status.h
%exclude /usr/include/google/protobuf/stubs/stl_util.h
%exclude /usr/include/google/protobuf/stubs/stringpiece.h
%exclude /usr/include/google/protobuf/stubs/template_util.h
%exclude /usr/include/google/protobuf/stubs/type_traits.h
%exclude /usr/include/google/protobuf/text_format.h
%exclude /usr/include/google/protobuf/timestamp.pb.h
%exclude /usr/include/google/protobuf/timestamp.proto
%exclude /usr/include/google/protobuf/type.pb.h
%exclude /usr/include/google/protobuf/type.proto
%exclude /usr/include/google/protobuf/unknown_field_set.h
%exclude /usr/include/google/protobuf/util/delimited_message_util.h
%exclude /usr/include/google/protobuf/util/field_comparator.h
%exclude /usr/include/google/protobuf/util/field_mask_util.h
%exclude /usr/include/google/protobuf/util/json_util.h
%exclude /usr/include/google/protobuf/util/message_differencer.h
%exclude /usr/include/google/protobuf/util/time_util.h
%exclude /usr/include/google/protobuf/util/type_resolver.h
%exclude /usr/include/google/protobuf/util/type_resolver_util.h
%exclude /usr/include/google/protobuf/wire_format.h
%exclude /usr/include/google/protobuf/wire_format_lite.h
%exclude /usr/include/google/protobuf/wire_format_lite_inl.h
%exclude /usr/include/google/protobuf/wrappers.pb.h
%exclude /usr/include/google/protobuf/wrappers.proto
%exclude /usr/lib64/libprotobuf-lite.so
%exclude /usr/lib64/libprotobuf.so
%exclude /usr/lib64/libprotoc.so
%exclude /usr/lib64/pkgconfig/protobuf-lite.pc
%exclude /usr/lib64/pkgconfig/protobuf.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libprotobuf-lite.so.14
/usr/lib64/libprotobuf-lite.so.14.0.0
/usr/lib64/libprotobuf.so.14
/usr/lib64/libprotobuf.so.14.0.0
/usr/lib64/libprotoc.so.14
/usr/lib64/libprotoc.so.14.0.0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
%exclude /usr/lib/python/site-packages/google/protobuf/__init__.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/__init__.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/any_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/any_test_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/api_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/descriptor.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/descriptor_database.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/descriptor_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/descriptor_pool.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/duration_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/empty_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/field_mask_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/json_format.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/map_unittest_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/message.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/message_factory.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/proto_builder.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/reflection.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/service.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/service_reflection.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/source_context_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/struct_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/symbol_database.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/test_messages_proto2_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/test_messages_proto3_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/text_encoding.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/text_format.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/timestamp_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/type_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/unittest_arena_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/unittest_custom_options_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/unittest_import_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/unittest_import_public_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/unittest_mset_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/unittest_mset_wire_format_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/unittest_no_arena_import_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/unittest_no_arena_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/unittest_no_generic_services_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/unittest_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/unittest_proto3_arena_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/__pycache__/wrappers_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/any_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/any_test_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/api_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/compiler/__init__.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/compiler/__pycache__/__init__.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/compiler/__pycache__/plugin_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/compiler/plugin_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/descriptor.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/descriptor_database.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/descriptor_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/descriptor_pool.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/duration_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/empty_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/field_mask_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__init__.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/__init__.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/_parameterized.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/any_test_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/api_implementation.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/containers.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/decoder.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/descriptor_database_test.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/descriptor_pool_test.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/descriptor_pool_test1_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/descriptor_pool_test2_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/descriptor_test.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/encoder.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/enum_type_wrapper.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/factory_test1_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/factory_test2_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/file_options_test_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/generator_test.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/json_format_test.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/message_factory_test.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/message_listener.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/message_set_extensions_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/message_test.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/missing_enum_values_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/more_extensions_dynamic_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/more_extensions_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/more_messages_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/packed_field_test_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/proto_builder_test.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/python_message.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/reflection_test.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/service_reflection_test.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/symbol_database_test.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/test_bad_identifiers_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/test_util.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/testing_refleaks.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/text_encoding_test.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/text_format_test.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/type_checkers.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/unknown_fields_test.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/well_known_types.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/well_known_types_test.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/wire_format.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/__pycache__/wire_format_test.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/_parameterized.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/any_test_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/api_implementation.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/containers.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/decoder.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/descriptor_database_test.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/descriptor_pool_test.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/descriptor_pool_test1_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/descriptor_pool_test2_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/descriptor_test.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/encoder.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/enum_type_wrapper.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/factory_test1_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/factory_test2_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/file_options_test_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/generator_test.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/import_test_package/__init__.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/import_test_package/__pycache__/__init__.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/import_test_package/__pycache__/inner_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/import_test_package/__pycache__/outer_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/import_test_package/inner_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/import_test_package/outer_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/json_format_test.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/message_factory_test.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/message_listener.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/message_set_extensions_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/message_test.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/missing_enum_values_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/more_extensions_dynamic_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/more_extensions_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/more_messages_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/packed_field_test_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/proto_builder_test.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/python_message.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/reflection_test.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/service_reflection_test.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/symbol_database_test.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/test_bad_identifiers_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/test_util.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/testing_refleaks.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/text_encoding_test.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/text_format_test.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/type_checkers.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/unknown_fields_test.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/well_known_types.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/well_known_types_test.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/wire_format.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/internal/wire_format_test.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/json_format.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/map_unittest_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/message.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/message_factory.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/proto_builder.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/pyext/__init__.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/pyext/__pycache__/__init__.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/pyext/__pycache__/cpp_message.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/pyext/__pycache__/python_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/pyext/cpp_message.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/pyext/python_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/reflection.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/service.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/service_reflection.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/source_context_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/struct_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/symbol_database.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/test_messages_proto2_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/test_messages_proto3_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/text_encoding.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/text_format.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/timestamp_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/type_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/unittest_arena_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/unittest_custom_options_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/unittest_import_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/unittest_import_public_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/unittest_mset_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/unittest_mset_wire_format_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/unittest_no_arena_import_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/unittest_no_arena_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/unittest_no_generic_services_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/unittest_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/unittest_proto3_arena_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/util/__init__.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/util/__pycache__/__init__.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/util/__pycache__/json_format_proto3_pb2.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/google/protobuf/util/json_format_proto3_pb2.py
%exclude /usr/lib/python3.7/site-packages/google/protobuf/wrappers_pb2.py
%exclude /usr/lib/python3.7/site-packages/protobuf-3.4.1-py3.7-nspkg.pth
%exclude /usr/lib/python3.7/site-packages/protobuf-3.4.1-py3.7.egg-info/PKG-INFO
%exclude /usr/lib/python3.7/site-packages/protobuf-3.4.1-py3.7.egg-info/SOURCES.txt
%exclude /usr/lib/python3.7/site-packages/protobuf-3.4.1-py3.7.egg-info/dependency_links.txt
%exclude /usr/lib/python3.7/site-packages/protobuf-3.4.1-py3.7.egg-info/namespace_packages.txt
%exclude /usr/lib/python3.7/site-packages/protobuf-3.4.1-py3.7.egg-info/requires.txt
%exclude /usr/lib/python3.7/site-packages/protobuf-3.4.1-py3.7.egg-info/top_level.txt
%exclude    /usr/lib/python3.7/site-packages/google/protobuf/__init__.py
