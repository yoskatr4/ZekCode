# ZekCode Projesi

Bu proje, kullanıcıların YouTube videolarını aramak ve belirli kod parçalarını bulmak için kullanılan bir Python uygulamasını içerir.

## Kullanım

1. **YouTube Araması (1):** Bu seçeneği seçerek, kullanıcıdan bir arama cümlesi alır ve YouTube'da bu cümleyi arar. İlk 5 video linkini gösterir.

2. **Code (2):** Bu seçeneği seçerek, belirli kod parçalarını bulabilirsiniz. Örneğin, "oyuncu kontrolü" veya "NPC nin karaktere göre yön değiştirmesi" gibi ifadeleri girebilir ve ilgili kodları elde edebilirsiniz.

3. **Çıkış (99):** Bu seçeneği seçerek programı sonlandırabilirsiniz.

## Örnek Kodlar

### Oyuncu Kontrolü

```gdscript
extends CharacterBody2D

@export var speed: int = 500

func handleInput():
    var moveDirection = Input.get_vector("ui_left","ui_right","ui_up","ui_down")
    velocity = moveDirection * speed

func _physics_process(delta):
    handleInput()
    if velocity.x == 500:
        $AnimationPlayer.play("right")
    if velocity.x == -500:
        $AnimationPlayer.play("left")
    if velocity.y == 500:
        $AnimationPlayer.play("down")
    if velocity.y == -500:
        $AnimationPlayer.play("up")
    move_and_slide()
```
## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylı bilgi için LICENSE dosyasını inceleyebilirsiniz.
