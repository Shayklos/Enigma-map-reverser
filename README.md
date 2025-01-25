This simple tool replaces an Enigma mapping like

```
CLASS DF RemappedClass
	FIELD field1162 remapped_field Ljava/lang/String; # Example comment
	METHOD method12 remapped_method (Ljava/lang/String;)V 
```

and turns it into

```
CLASS RemappedClass DF
	FIELD remapped_field field1162 Ljava/lang/String; # Example comment
	METHOD remapped_method method12 (Ljava/lang/String;)V 
```

### Use

```
python enigma_reverser.py path/to/input_file path/to/output_file
```