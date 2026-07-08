# SDK Sankhya — Mapeamento de Objetos com MapStruct

> **Acesso Antecipado (Beta):** APIs sujeitas a modificações. Sem suporte para Kotlin.

## O que é

Integração nativa com **MapStruct** para mapeamento entre DTOs, entidades JAPE e outros beans. O MapStruct gera a implementação em tempo de compilação — sem reflection, sem boilerplate.

O SDK detecta automaticamente o MapStruct no classpath. Se presente, ativa a integração e registra os mappers no contêiner de DI. Se ausente, ignora sem erros.

---

## Configuração

```groovy
// build.gradle
dependencies {
    implementation 'org.mapstruct:mapstruct:1.5.5.Final'
    annotationProcessor 'org.mapstruct:mapstruct-processor:1.5.5.Final'
}

tasks.withType(JavaCompile) {
    options.compilerArgs += [
        '-Amapstruct.defaultComponentModel=cdi',
        '-Amapstruct.unmappedTargetPolicy=IGNORE'
    ]
}
```

---

## Como Usar

### 1. Crie a interface do Mapper

```java
@Mapper(componentModel = "cdi")
public interface UserMapper {

    @Mapping(source = "nomeUsuario", target = "username")
    @Mapping(source = "ativo", target = "enabled")
    UserDTO toDTO(UserJapeEntity entity);

    @Mapping(target = "nomeUsuario", source = "username")
    @Mapping(target = "ativo", source = "enabled")
    UserJapeEntity toEntity(UserDTO dto);

    List<UserDTO> toDTOList(List<UserJapeEntity> entities);
}
```

### 2. Injete o Mapper via `@Inject`

```java
@Component
public class UserService {

    private final UserRepository userRepository;
    private final UserMapper userMapper;

    @Inject
    public UserService(UserRepository userRepository, UserMapper userMapper) {
        this.userRepository = userRepository;
        this.userMapper = userMapper;
    }

    @Transactional
    public UserDTO findUserById(Long userId) {
        UserJapeEntity entity = userRepository.findByPK(userId)
            .orElseThrow(() -> new NotFoundException("Usuário não encontrado"));
        return userMapper.toDTO(entity);
    }

    public void createUser(UserDTO dto) {
        userRepository.save(userMapper.toEntity(dto));
    }
}
```

> O SDK registra automaticamente o mapper gerado no contêiner de DI — nenhuma configuração adicional necessária.

---

## Uso com campos `@Lazy`

Campos anotados com `@Lazy` em entidades não são serializados automaticamente pelo Gson (que usa fields, não getters). Use MapStruct para converter para DTO antes de retornar em controllers.

---

## Troubleshooting

**Mapper não está sendo injetado (`UnsatisfiedDependencyException`):**
- Verifique se `mapstruct-processor` está em `annotationProcessor` (não em `implementation`)
- Confirme `componentModel = "cdi"` ou `"default"` na anotação `@Mapper`
- Force recompilação: `./gradlew clean build`

**Processador não roda:**
- Limpe o cache: `./gradlew clean --refresh-dependencies`

---

## Fonte

https://developer.sankhya.com.br/docs/%EF%B8%8Fmapeamento-de-objetos-com-mapstruct
