from googlesearch import search
import time as t
import difflib
print('''
 / \---------------, 
 \_,|              | 
    |    ZekCode   | 
    |  ,-------------
    \_/____________/ 
      
      1 : Youtube araması
      2 : Code 
      99 : Çıkış
''')
a = int(input(""))
if a == 1:
    def search_youtube_videos(query):
        # YouTube videolarını ara
        search_query = query + " site:youtube.com"
        search_results = search(search_query, num_results=5)

        # İlk 5 videonun linklerini yazdır
        for i, result in enumerate(search_results, start=1):
            print(f"Video {i}: {result}")

    # Kullanıcıdan arama cümlesi al
    user_query = input("Aramak istediğiniz cümleyi girin: ")

    # YouTube videolarını ara ve linkleri yazdır
    search_youtube_videos(user_query)
if a == 2:
    def benzer_kelime_bul(girdi, hedef_kelime, esik_deger=0.8):
        benzerlik = difflib.SequenceMatcher(None, girdi.lower(), hedef_kelime.lower()).ratio()
        return benzerlik > esik_deger
    
    print("Ne kodu istiyorsunuz(sadece godot4 destekliyor)")
    print("Örenk : oyuncu kontrolü, NPC nin karaktere göre yön değiştirmesi")
    m = str(input("> "))
    if benzer_kelime_bul(m, "oyuncu kontrolü"):
        print('''
extends CharacterBody2D

@export var speed: int = 500


func handleInput():
	var moveDirection = Input.get_vector("ui_left","ui_right","ui_up","ui_down")
	velocity = moveDirection*speed
	
func  _physics_process(delta):
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
''')

    if benzer_kelime_bul(m, "NPC nin karaktere göre yön değiştirmesi"):
        print('''
extends Area2D

var is_inside_area := false

func _process(delta):
	if is_inside_area and Input.is_action_pressed("e"):
		print("owwyeah")

func _on_area_entered(area):
	is_inside_area = true


func _on_area_exited(area):
	is_inside_area = false


func _on_body_entered(body):
	if global_position.x > body.global_position.x:
		$Sprite2D.flip_h = false
	else:
		$Sprite2D.flip_h = true)
''')
if a == 99:
    print("Tekrar bekleriz...")
    t.sleep(3)
    exit()
