INSERT INTO dojos (name)
VALUES ("Chicago"), ("Seattle"),("Online");


SET SQL_SAFE_UPDATES = 0;
DELETE FROM dojos;


INSERT INTO ninjas (first_name,last_name,age,dojo_id)
VALUES ("Adrien","Dion",39,4),("Anne","Jurack",34,4),("Ryan","Magley",30,4);


INSERT INTO ninjas (first_name,last_name,age,dojo_id)
VALUES ("Marisa","Goode",37,5),("Todd","Enders",36,5),("Sadie","Flick",29,5);


INSERT INTO ninjas (first_name,last_name,age,dojo_id)
VALUES ("Mr. Nibbles","Pancakes",54,6),("Benny Bob","McBob",65,6),("Mitch","Golden",26,6);


SELECT * FROM dojos
LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
WHERE dojos.id = 4;


SELECT * FROM dojos
LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
WHERE dojos.id = (SELECT id FROM dojos ORDER BY id DESC LIMIT 1);


SELECT * FROM dojos
WHERE dojos.id = (SELECT dojo_id FROM ninjas ORDER BY dojo_id DESC LIMIT 1);