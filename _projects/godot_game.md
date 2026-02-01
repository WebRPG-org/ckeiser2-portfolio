---
title: 🎮 Godot Game [2048 Knight] 🕹️
#permalink: /games/:name/
category: games 🎮
#tools: [C#, Designer, Programmer, Godot]
img: assets/pngs/godot.png
layout: page
description: C# in Godot Engine, Designed the UI and multiple systems.

---
## Skills Showcased
*Godot:* *In-Engine Tools* 
*- Languages:C#*

##### Role: System Designer // UI Programmer


**Description**
Group project using Godot (A game engine that uses C#) where I served as lead designer. Original concept for 2048 Knight was an RPG interpretation of the mobile game 2048 essentially inspired by its grid based desgin. Some of my roles on the team involved designing the UI and multiple systems. As the scope for the project was only a few weeks of the course the scope was incredibly small especially when considering learning an engine in that time. But showcases my role as designer in which I created proof of concepts through desgin documents. Addtionally, implemented the final UI for the game, including the health bar, inventory system and more. Attached below is a link to google drive that shows design documents and process along with a short demo.

<iframe width="560" height="315"
    src="https://www.youtube.com/embed/8eQsWIewl-M"
    frameborder="0"
    allowfullscreen>
</iframe>

### 🛠 Scripts I wrote

As the designer I aided in the completion of our design documents but additionally, with my technical background, implemented a few core systems to aid the developers on the team including the pause/quit menu, item and inventory systems.

---

📁 **Godot Scripts**

##### Helper functions for Pause Menu
- [pause_menu.gd]( {{ site.baseurl }}/assets/godot/scripts/pause_menu.gd )
<img src="{{ site.baseurl }}/assets/godot/assets/pause_menu.png" alt="Pause Menu>

```cs
extends Control

@onready var main = $"../../"


func _on_resume_pressed():
	main.pauseMenu()


func _on_quit_pressed():
	get_tree().quit()
```

##### Place holder player character for testing purposes
- [player.gd]( {{ site.baseurl }}/assets/godot/scripts/player.gd )

```cs
extends CharacterBody2D

@export var MAX_SPEED = 300
@export var ACCELERATION = 1500
@export var FRICTION = 1200

@onready var axis = Vector2.ZERO



func _physics_process(delta):
	move(delta)

func get_input_axis():
	axis.x=int(Input.is_action_pressed("move_right")) - int(Input.is_action_pressed("move_left"))
	axis.y=int(Input.is_action_pressed("move_down")) - int(Input.is_action_pressed("move_up"))
	return axis.normalized()


func move(delta):
	
	axis = get_input_axis()
	
	if axis == Vector2.ZERO:
		apply_friction(FRICTION * delta)
		pass #apply friction
		
	else:
		apply_movement(axis * ACCELERATION * delta)
		pass #apply movement
		
	move_and_slide()
	
func apply_friction(amount):
	if velocity.length() > amount:
		velocity -= velocity.normalized() * amount
		
	else:
		velocity = Vector2.ZERO
		
func apply_movement(accel):
	velocity += accel
	velocity = velocity.limit_length(MAX_SPEED)
```
##### Main PauseMenu testing script
- [PauseMenu.gd]( {{ site.baseurl }}/assets/godot/scripts/PauseMenu.gd )

```cs

extends Node2D

@onready var PauseMenu = $Camera2D/PauseMenu
var paused = false

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	if Input.is_action_just_pressed("pause"):
		pauseMenu()
		
		
func pauseMenu():
	if paused:
		PauseMenu.hide()
		Engine.time_scale = 1
	else:
		PauseMenu.show()
		Engine.time_scale = 0
			
	paused= !paused

```

##### Rewritten Pausemenu scripts to accommodate for LTS Godot version
- [PauseMenu2.gd]( {{ site.baseurl }}/assets/godot/scripts/PauseMenu2.gd )

```cs

extends Control

var is_paused = false setget set_is_paused

func _unhandled_input(event):
	if event.is_action_pressed("pause"):
		self.is_paused = !is_paused

func set_is_paused(value):
	is_paused = value
	get_tree().paused = is_paused
	visible = is_paused




func _on_Resume_pressed():
	self.is_paused = false


func _on_Quit_pressed():
	get_tree().quit()

```

- [PauseMenu2.tscn]( {{ site.baseurl }}/assets/godot/scripts/PauseMenu2.tscn )

```cs
[gd_scene load_steps=2 format=2]

[ext_resource path="res://PauseMenu2.gd" type="Script" id=1]

[node name="PauseMenu2" type="Control"]
visible = false
anchor_right = 1.0
anchor_bottom = 1.0
script = ExtResource( 1 )

[node name="ColorRect" type="ColorRect" parent="."]
anchor_right = 1.0
anchor_bottom = 1.0
color = Color( 0.231373, 0.298039, 0.286275, 0.368627 )

[node name="CenterContainer" type="CenterContainer" parent="."]
anchor_right = 1.0
anchor_bottom = 1.0

[node name="VBoxContainer" type="VBoxContainer" parent="CenterContainer"]
margin_left = 835.0
margin_top = 463.0
margin_right = 1085.0
margin_bottom = 617.0
custom_constants/separation = 30

[node name="PauseText" type="Label" parent="CenterContainer/VBoxContainer"]
margin_right = 250.0
margin_bottom = 14.0
rect_min_size = Vector2( 20, 0 )
text = "Paused"
align = 1

[node name="Control" type="Control" parent="CenterContainer/VBoxContainer"]
margin_top = 44.0
margin_right = 250.0
margin_bottom = 54.0
rect_min_size = Vector2( 0, 10 )

[node name="Resume" type="Button" parent="CenterContainer/VBoxContainer"]
margin_top = 84.0
margin_right = 250.0
margin_bottom = 104.0
rect_min_size = Vector2( 250, 0 )
text = "Resume"

[node name="Quit" type="Button" parent="CenterContainer/VBoxContainer"]
margin_top = 134.0
margin_right = 250.0
margin_bottom = 154.0
text = "Quit"

[connection signal="pressed" from="CenterContainer/VBoxContainer/Resume" to="." method="_on_Resume_pressed"]
[connection signal="pressed" from="CenterContainer/VBoxContainer/Quit" to="." method="_on_Quit_pressed"]
```


##### Inventory and item system scripts
- [inventory.gd]( {{ site.baseurl }}/assets/godot/scripts/inventory.gd )

```cs
extends Node2D

const SlotClass = preload("res://Slot1.gd")
onready var inventory_slots = $GridContainer
var holding_item = null

func _ready():
	for inv_slot in inventory_slots.get_children():
		inv_slot.connect("gui_input", self, "slot_gui_input", [inv_slot])
		
func slot_gui_input(event: InputEvent, slot: SlotClass):
	if event is InputEventMouseButton:
		if event.button_index == BUTTON_LEFT && event.pressed:
			if holding_item != null:
				if !slot.item:
					slot.putIntoSlot(holding_item)
					holding_item = null
				else:
					var temp_item = slot.item
					slot.pickFromSlot()
					temp_item.global_position = event.global_position
					slot.putIntoSlot(holding_item)
					holding_item = temp_item
			elif slot.item:
				holding_item = slot.item
				slot.pickFromSlot()
				holding_item.global_position = get_global_mouse_position()
					
func _input(event):
	if holding_item:
		holding_item.global_position = get_global_mouse_position()
```

- [inventory.tscn]( {{ site.baseurl }}/assets/godot/scripts/inventory.tscn )

```cs
[gd_scene load_steps=6 format=2]

[ext_resource path="res://default_inventory_background.png" type="Texture" id=1]
[ext_resource path="res://item_slot_default_background.png" type="Texture" id=2]
[ext_resource path="res://Slot1.gd" type="Script" id=3]
[ext_resource path="res://Inventory.gd" type="Script" id=4]

[sub_resource type="StyleBoxTexture" id=1]
texture = ExtResource( 2 )
region_rect = Rect2( 0, 0, 18, 18 )

[node name="Inventory" type="Node2D"]
script = ExtResource( 4 )

[node name="TextureRect" type="TextureRect" parent="."]
anchor_left = 0.5
anchor_top = 0.5
anchor_right = 0.5
anchor_bottom = 0.5
margin_left = 149.0
margin_top = 83.0
margin_right = 460.0
margin_bottom = 259.0
texture = ExtResource( 1 )

[node name="GridContainer" type="GridContainer" parent="."]
anchor_left = 0.5
anchor_top = 0.5
anchor_right = 0.5
anchor_bottom = 0.5
margin_left = 236.0
margin_top = 105.0
margin_right = 353.0
margin_bottom = 194.0
custom_constants/vseparation = 5
custom_constants/hseparation = 5
columns = 4

[node name="Slot1" type="Panel" parent="GridContainer"]
margin_right = 25.0
margin_bottom = 25.0
rect_min_size = Vector2( 25, 25 )
custom_styles/panel = SubResource( 1 )
script = ExtResource( 3 )

[node name="Slot2" type="Panel" parent="GridContainer"]
margin_left = 30.0
margin_right = 55.0
margin_bottom = 25.0
rect_min_size = Vector2( 25, 25 )
custom_styles/panel = SubResource( 1 )
script = ExtResource( 3 )

[node name="Slot3" type="Panel" parent="GridContainer"]
margin_left = 60.0
margin_right = 85.0
margin_bottom = 25.0
rect_min_size = Vector2( 25, 25 )
custom_styles/panel = SubResource( 1 )
script = ExtResource( 3 )

[node name="Slot4" type="Panel" parent="GridContainer"]
margin_left = 90.0
margin_right = 115.0
margin_bottom = 25.0
rect_min_size = Vector2( 25, 25 )
custom_styles/panel = SubResource( 1 )
script = ExtResource( 3 )

[node name="Slot5" type="Panel" parent="GridContainer"]
margin_top = 30.0
margin_right = 25.0
margin_bottom = 55.0
rect_min_size = Vector2( 25, 25 )
custom_styles/panel = SubResource( 1 )
script = ExtResource( 3 )

[node name="Slot6" type="Panel" parent="GridContainer"]
margin_left = 30.0
margin_top = 30.0
margin_right = 55.0
margin_bottom = 55.0
rect_min_size = Vector2( 25, 25 )
custom_styles/panel = SubResource( 1 )
script = ExtResource( 3 )

[node name="Slot7" type="Panel" parent="GridContainer"]
margin_left = 60.0
margin_top = 30.0
margin_right = 85.0
margin_bottom = 55.0
rect_min_size = Vector2( 25, 25 )
custom_styles/panel = SubResource( 1 )
script = ExtResource( 3 )

[node name="Slot8" type="Panel" parent="GridContainer"]
margin_left = 90.0
margin_top = 30.0
margin_right = 115.0
margin_bottom = 55.0
rect_min_size = Vector2( 25, 25 )
custom_styles/panel = SubResource( 1 )
script = ExtResource( 3 )

[node name="Slot9" type="Panel" parent="GridContainer"]
margin_top = 60.0
margin_right = 25.0
margin_bottom = 85.0
rect_min_size = Vector2( 25, 25 )
custom_styles/panel = SubResource( 1 )
script = ExtResource( 3 )

[node name="Slot10" type="Panel" parent="GridContainer"]
margin_left = 30.0
margin_top = 60.0
margin_right = 55.0
margin_bottom = 85.0
rect_min_size = Vector2( 25, 25 )
custom_styles/panel = SubResource( 1 )
script = ExtResource( 3 )

[node name="Slot11" type="Panel" parent="GridContainer"]
margin_left = 60.0
margin_top = 60.0
margin_right = 85.0
margin_bottom = 85.0
rect_min_size = Vector2( 25, 25 )
custom_styles/panel = SubResource( 1 )
script = ExtResource( 3 )

[node name="Slot12" type="Panel" parent="GridContainer"]
margin_left = 90.0
margin_top = 60.0
margin_right = 115.0
margin_bottom = 85.0
rect_min_size = Vector2( 25, 25 )
custom_styles/panel = SubResource( 1 )
script = ExtResource( 3 )

```

#### Item script only takes into account two different items for testing beta purposes
- [item.gd]( {{ site.baseurl }}/assets/godot/scripts/item.gd )

```gdscript

extends Node2D

func _ready():
	if randi() % 2 == 0:
		$TextureRect.texture = load("res://Slime Potion.png")
	else:
		$TextureRect.texture = load("res://Tree Branch.png")

```

- [item.tscn]( {{ site.baseurl }}/assets/godot/scripts/item.tscn )

```cs

[gd_scene load_steps=3 format=2]

[ext_resource path="res://Item.gd" type="Script" id=1]
[ext_resource path="res://Slime Potion.png" type="Texture" id=2]

[node name="Item" type="Node2D"]
z_index = 1
script = ExtResource( 1 )

[node name="TextureRect" type="TextureRect" parent="."]
margin_right = 40.0
margin_bottom = 40.0
mouse_filter = 2
texture = ExtResource( 2 )

```


#### Updates the item slots animation depending on if an item is placed in it or not
- [slot1.gd]( {{ site.baseurl }}/assets/godot/scripts/slot1.gd )

```cs

extends Panel

var default_tex = preload("res://item_slot_default_background.png")
var empty_tex = preload("res://item_slot_empty_background.png")
var default_style: StyleBoxTexture = null
var empty_style: StyleBoxTexture = null

var ItemClass = preload("res://Item.tscn")
var item = null

func _ready():
	default_style = StyleBoxTexture.new()
	empty_style = StyleBoxTexture.new()
	default_style.texture = default_tex
	empty_style.texture = empty_tex
	
	
	if randi() % 2 == 0:
		item = ItemClass.instance()
		add_child(item)
	refresh_style()

func pickFromSlot():
	remove_child(item)
	var inventoryNode = find_parent('Inventory')
	inventoryNode.add_child(item)
	item = null
	refresh_style()
	
func putIntoSlot(new_item):
	item = new_item
	item.position = Vector2(0,0)
	var inventoryNode = find_parent("Inventory")
	inventoryNode.remove_child(item)
	add_child(item)
	refresh_style()	

func refresh_style():
	if item == null:
		set('custom_styles/panel', empty_style)
	else:
		set('custom_styles/panel', default_style)
```

##### Link to google drive w/ Design Docs
<div class="left">
{% include elements/button.html link="https://drive.google.com/drive/folders/1K3kAyzcWXABthIY7s9kPn_uHCcTR0HU6?usp=sharing" text="Google Drive with Design Documents" %}
</div>

##### Link to github repo/ project code
<div class="right">
{% include elements/button.html link="https://github.com/LukeAlbarracin/2048-Knight/tree/main" text="Github Repo" %}
</div>