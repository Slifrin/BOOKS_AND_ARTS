// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: weather.proto

#include "weather.pb.h"

#include <algorithm>

#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/extension_set.h>
#include <google/protobuf/wire_format_lite.h>
#include <google/protobuf/descriptor.h>
#include <google/protobuf/generated_message_reflection.h>
#include <google/protobuf/reflection_ops.h>
#include <google/protobuf/wire_format.h>
// @@protoc_insertion_point(includes)
#include <google/protobuf/port_def.inc>

PROTOBUF_PRAGMA_INIT_SEG

namespace _pb = ::PROTOBUF_NAMESPACE_ID;
namespace _pbi = _pb::internal;

namespace pd {
constexpr Temperature::Temperature(
    ::_pbi::ConstantInitialized)
  : station_(&::_pbi::fixed_address_empty_string, ::_pbi::ConstantInitialized{})
  , time_(nullptr)
  , value_(0){}
struct TemperatureDefaultTypeInternal {
  constexpr TemperatureDefaultTypeInternal()
      : _instance(::_pbi::ConstantInitialized{}) {}
  ~TemperatureDefaultTypeInternal() {}
  union {
    Temperature _instance;
  };
};
PROTOBUF_ATTRIBUTE_NO_DESTROY PROTOBUF_CONSTINIT PROTOBUF_ATTRIBUTE_INIT_PRIORITY1 TemperatureDefaultTypeInternal _Temperature_default_instance_;
}  // namespace pd
static ::_pb::Metadata file_level_metadata_weather_2eproto[1];
static constexpr ::_pb::EnumDescriptor const** file_level_enum_descriptors_weather_2eproto = nullptr;
static constexpr ::_pb::ServiceDescriptor const** file_level_service_descriptors_weather_2eproto = nullptr;

const uint32_t TableStruct_weather_2eproto::offsets[] PROTOBUF_SECTION_VARIABLE(protodesc_cold) = {
  ~0u,  // no _has_bits_
  PROTOBUF_FIELD_OFFSET(::pd::Temperature, _internal_metadata_),
  ~0u,  // no _extensions_
  ~0u,  // no _oneof_case_
  ~0u,  // no _weak_field_map_
  ~0u,  // no _inlined_string_donated_
  PROTOBUF_FIELD_OFFSET(::pd::Temperature, time_),
  PROTOBUF_FIELD_OFFSET(::pd::Temperature, station_),
  PROTOBUF_FIELD_OFFSET(::pd::Temperature, value_),
};
static const ::_pbi::MigrationSchema schemas[] PROTOBUF_SECTION_VARIABLE(protodesc_cold) = {
  { 0, -1, -1, sizeof(::pd::Temperature)},
};

static const ::_pb::Message* const file_default_instances[] = {
  &::pd::_Temperature_default_instance_._instance,
};

const char descriptor_table_protodef_weather_2eproto[] PROTOBUF_SECTION_VARIABLE(protodesc_cold) =
  "\n\rweather.proto\022\002pd\032\037google/protobuf/tim"
  "estamp.proto\"W\n\013Temperature\022(\n\004time\030\001 \001("
  "\0132\032.google.protobuf.Timestamp\022\017\n\007station"
  "\030\002 \001(\t\022\r\n\005value\030\003 \001(\001b\006proto3"
  ;
static const ::_pbi::DescriptorTable* const descriptor_table_weather_2eproto_deps[1] = {
  &::descriptor_table_google_2fprotobuf_2ftimestamp_2eproto,
};
static ::_pbi::once_flag descriptor_table_weather_2eproto_once;
const ::_pbi::DescriptorTable descriptor_table_weather_2eproto = {
    false, false, 149, descriptor_table_protodef_weather_2eproto,
    "weather.proto",
    &descriptor_table_weather_2eproto_once, descriptor_table_weather_2eproto_deps, 1, 1,
    schemas, file_default_instances, TableStruct_weather_2eproto::offsets,
    file_level_metadata_weather_2eproto, file_level_enum_descriptors_weather_2eproto,
    file_level_service_descriptors_weather_2eproto,
};
PROTOBUF_ATTRIBUTE_WEAK const ::_pbi::DescriptorTable* descriptor_table_weather_2eproto_getter() {
  return &descriptor_table_weather_2eproto;
}

// Force running AddDescriptors() at dynamic initialization time.
PROTOBUF_ATTRIBUTE_INIT_PRIORITY2 static ::_pbi::AddDescriptorsRunner dynamic_init_dummy_weather_2eproto(&descriptor_table_weather_2eproto);
namespace pd {

// ===================================================================

class Temperature::_Internal {
 public:
  static const ::PROTOBUF_NAMESPACE_ID::Timestamp& time(const Temperature* msg);
};

const ::PROTOBUF_NAMESPACE_ID::Timestamp&
Temperature::_Internal::time(const Temperature* msg) {
  return *msg->time_;
}
void Temperature::clear_time() {
  if (GetArenaForAllocation() == nullptr && time_ != nullptr) {
    delete time_;
  }
  time_ = nullptr;
}
Temperature::Temperature(::PROTOBUF_NAMESPACE_ID::Arena* arena,
                         bool is_message_owned)
  : ::PROTOBUF_NAMESPACE_ID::Message(arena, is_message_owned) {
  SharedCtor();
  // @@protoc_insertion_point(arena_constructor:pd.Temperature)
}
Temperature::Temperature(const Temperature& from)
  : ::PROTOBUF_NAMESPACE_ID::Message() {
  _internal_metadata_.MergeFrom<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(from._internal_metadata_);
  station_.InitDefault();
  #ifdef PROTOBUF_FORCE_COPY_DEFAULT_STRING
    station_.Set("", GetArenaForAllocation());
  #endif // PROTOBUF_FORCE_COPY_DEFAULT_STRING
  if (!from._internal_station().empty()) {
    station_.Set(from._internal_station(), 
      GetArenaForAllocation());
  }
  if (from._internal_has_time()) {
    time_ = new ::PROTOBUF_NAMESPACE_ID::Timestamp(*from.time_);
  } else {
    time_ = nullptr;
  }
  value_ = from.value_;
  // @@protoc_insertion_point(copy_constructor:pd.Temperature)
}

inline void Temperature::SharedCtor() {
station_.InitDefault();
#ifdef PROTOBUF_FORCE_COPY_DEFAULT_STRING
  station_.Set("", GetArenaForAllocation());
#endif // PROTOBUF_FORCE_COPY_DEFAULT_STRING
::memset(reinterpret_cast<char*>(this) + static_cast<size_t>(
    reinterpret_cast<char*>(&time_) - reinterpret_cast<char*>(this)),
    0, static_cast<size_t>(reinterpret_cast<char*>(&value_) -
    reinterpret_cast<char*>(&time_)) + sizeof(value_));
}

Temperature::~Temperature() {
  // @@protoc_insertion_point(destructor:pd.Temperature)
  if (auto *arena = _internal_metadata_.DeleteReturnArena<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>()) {
  (void)arena;
    return;
  }
  SharedDtor();
}

inline void Temperature::SharedDtor() {
  GOOGLE_DCHECK(GetArenaForAllocation() == nullptr);
  station_.Destroy();
  if (this != internal_default_instance()) delete time_;
}

void Temperature::SetCachedSize(int size) const {
  _cached_size_.Set(size);
}

void Temperature::Clear() {
// @@protoc_insertion_point(message_clear_start:pd.Temperature)
  uint32_t cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  station_.ClearToEmpty();
  if (GetArenaForAllocation() == nullptr && time_ != nullptr) {
    delete time_;
  }
  time_ = nullptr;
  value_ = 0;
  _internal_metadata_.Clear<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>();
}

const char* Temperature::_InternalParse(const char* ptr, ::_pbi::ParseContext* ctx) {
#define CHK_(x) if (PROTOBUF_PREDICT_FALSE(!(x))) goto failure
  while (!ctx->Done(&ptr)) {
    uint32_t tag;
    ptr = ::_pbi::ReadTag(ptr, &tag);
    switch (tag >> 3) {
      // .google.protobuf.Timestamp time = 1;
      case 1:
        if (PROTOBUF_PREDICT_TRUE(static_cast<uint8_t>(tag) == 10)) {
          ptr = ctx->ParseMessage(_internal_mutable_time(), ptr);
          CHK_(ptr);
        } else
          goto handle_unusual;
        continue;
      // string station = 2;
      case 2:
        if (PROTOBUF_PREDICT_TRUE(static_cast<uint8_t>(tag) == 18)) {
          auto str = _internal_mutable_station();
          ptr = ::_pbi::InlineGreedyStringParser(str, ptr, ctx);
          CHK_(ptr);
          CHK_(::_pbi::VerifyUTF8(str, "pd.Temperature.station"));
        } else
          goto handle_unusual;
        continue;
      // double value = 3;
      case 3:
        if (PROTOBUF_PREDICT_TRUE(static_cast<uint8_t>(tag) == 25)) {
          value_ = ::PROTOBUF_NAMESPACE_ID::internal::UnalignedLoad<double>(ptr);
          ptr += sizeof(double);
        } else
          goto handle_unusual;
        continue;
      default:
        goto handle_unusual;
    }  // switch
  handle_unusual:
    if ((tag == 0) || ((tag & 7) == 4)) {
      CHK_(ptr);
      ctx->SetLastTag(tag);
      goto message_done;
    }
    ptr = UnknownFieldParse(
        tag,
        _internal_metadata_.mutable_unknown_fields<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(),
        ptr, ctx);
    CHK_(ptr != nullptr);
  }  // while
message_done:
  return ptr;
failure:
  ptr = nullptr;
  goto message_done;
#undef CHK_
}

uint8_t* Temperature::_InternalSerialize(
    uint8_t* target, ::PROTOBUF_NAMESPACE_ID::io::EpsCopyOutputStream* stream) const {
  // @@protoc_insertion_point(serialize_to_array_start:pd.Temperature)
  uint32_t cached_has_bits = 0;
  (void) cached_has_bits;

  // .google.protobuf.Timestamp time = 1;
  if (this->_internal_has_time()) {
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::
      InternalWriteMessage(1, _Internal::time(this),
        _Internal::time(this).GetCachedSize(), target, stream);
  }

  // string station = 2;
  if (!this->_internal_station().empty()) {
    ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::VerifyUtf8String(
      this->_internal_station().data(), static_cast<int>(this->_internal_station().length()),
      ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::SERIALIZE,
      "pd.Temperature.station");
    target = stream->WriteStringMaybeAliased(
        2, this->_internal_station(), target);
  }

  // double value = 3;
  static_assert(sizeof(uint64_t) == sizeof(double), "Code assumes uint64_t and double are the same size.");
  double tmp_value = this->_internal_value();
  uint64_t raw_value;
  memcpy(&raw_value, &tmp_value, sizeof(tmp_value));
  if (raw_value != 0) {
    target = stream->EnsureSpace(target);
    target = ::_pbi::WireFormatLite::WriteDoubleToArray(3, this->_internal_value(), target);
  }

  if (PROTOBUF_PREDICT_FALSE(_internal_metadata_.have_unknown_fields())) {
    target = ::_pbi::WireFormat::InternalSerializeUnknownFieldsToArray(
        _internal_metadata_.unknown_fields<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(::PROTOBUF_NAMESPACE_ID::UnknownFieldSet::default_instance), target, stream);
  }
  // @@protoc_insertion_point(serialize_to_array_end:pd.Temperature)
  return target;
}

size_t Temperature::ByteSizeLong() const {
// @@protoc_insertion_point(message_byte_size_start:pd.Temperature)
  size_t total_size = 0;

  uint32_t cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  // string station = 2;
  if (!this->_internal_station().empty()) {
    total_size += 1 +
      ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::StringSize(
        this->_internal_station());
  }

  // .google.protobuf.Timestamp time = 1;
  if (this->_internal_has_time()) {
    total_size += 1 +
      ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::MessageSize(
        *time_);
  }

  // double value = 3;
  static_assert(sizeof(uint64_t) == sizeof(double), "Code assumes uint64_t and double are the same size.");
  double tmp_value = this->_internal_value();
  uint64_t raw_value;
  memcpy(&raw_value, &tmp_value, sizeof(tmp_value));
  if (raw_value != 0) {
    total_size += 1 + 8;
  }

  return MaybeComputeUnknownFieldsSize(total_size, &_cached_size_);
}

const ::PROTOBUF_NAMESPACE_ID::Message::ClassData Temperature::_class_data_ = {
    ::PROTOBUF_NAMESPACE_ID::Message::CopyWithSizeCheck,
    Temperature::MergeImpl
};
const ::PROTOBUF_NAMESPACE_ID::Message::ClassData*Temperature::GetClassData() const { return &_class_data_; }

void Temperature::MergeImpl(::PROTOBUF_NAMESPACE_ID::Message* to,
                      const ::PROTOBUF_NAMESPACE_ID::Message& from) {
  static_cast<Temperature *>(to)->MergeFrom(
      static_cast<const Temperature &>(from));
}


void Temperature::MergeFrom(const Temperature& from) {
// @@protoc_insertion_point(class_specific_merge_from_start:pd.Temperature)
  GOOGLE_DCHECK_NE(&from, this);
  uint32_t cached_has_bits = 0;
  (void) cached_has_bits;

  if (!from._internal_station().empty()) {
    _internal_set_station(from._internal_station());
  }
  if (from._internal_has_time()) {
    _internal_mutable_time()->::PROTOBUF_NAMESPACE_ID::Timestamp::MergeFrom(from._internal_time());
  }
  static_assert(sizeof(uint64_t) == sizeof(double), "Code assumes uint64_t and double are the same size.");
  double tmp_value = from._internal_value();
  uint64_t raw_value;
  memcpy(&raw_value, &tmp_value, sizeof(tmp_value));
  if (raw_value != 0) {
    _internal_set_value(from._internal_value());
  }
  _internal_metadata_.MergeFrom<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(from._internal_metadata_);
}

void Temperature::CopyFrom(const Temperature& from) {
// @@protoc_insertion_point(class_specific_copy_from_start:pd.Temperature)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool Temperature::IsInitialized() const {
  return true;
}

void Temperature::InternalSwap(Temperature* other) {
  using std::swap;
  auto* lhs_arena = GetArenaForAllocation();
  auto* rhs_arena = other->GetArenaForAllocation();
  _internal_metadata_.InternalSwap(&other->_internal_metadata_);
  ::PROTOBUF_NAMESPACE_ID::internal::ArenaStringPtr::InternalSwap(
      &station_, lhs_arena,
      &other->station_, rhs_arena
  );
  ::PROTOBUF_NAMESPACE_ID::internal::memswap<
      PROTOBUF_FIELD_OFFSET(Temperature, value_)
      + sizeof(Temperature::value_)
      - PROTOBUF_FIELD_OFFSET(Temperature, time_)>(
          reinterpret_cast<char*>(&time_),
          reinterpret_cast<char*>(&other->time_));
}

::PROTOBUF_NAMESPACE_ID::Metadata Temperature::GetMetadata() const {
  return ::_pbi::AssignDescriptors(
      &descriptor_table_weather_2eproto_getter, &descriptor_table_weather_2eproto_once,
      file_level_metadata_weather_2eproto[0]);
}

// @@protoc_insertion_point(namespace_scope)
}  // namespace pd
PROTOBUF_NAMESPACE_OPEN
template<> PROTOBUF_NOINLINE ::pd::Temperature*
Arena::CreateMaybeMessage< ::pd::Temperature >(Arena* arena) {
  return Arena::CreateMessageInternal< ::pd::Temperature >(arena);
}
PROTOBUF_NAMESPACE_CLOSE

// @@protoc_insertion_point(global_scope)
#include <google/protobuf/port_undef.inc>
