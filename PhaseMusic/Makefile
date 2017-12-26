.PHONY: clean tests

tests:
	javac -d src/test/ src/test/java/*.java

clean:
	#Add Dummy files to prevent rm errors
	touch src/main/dummy.class
	touch src/test/dummy.class
	rm src/main/*.class
	rm src/test/*.class
