# 🎯 Learn Python
Learn Python basics from code with josh youtube channel and other free youtube courses
## 🎯 About The OOP In Python
1- How Name Mangling Works
--------------------------
In Python, when you prefix an attribute with double underscores (e.g., __balance), Python performs a process called Name Mangling.
It isn’t strictly "private" like in Java or C++, but Python internally renames the variable to make it harder to accidentally access or override.
When Python sees __field inside a class named Account, it automatically changes the name to:
_ClassName__field (e.g., _Account__balance).

2- Why does Python do this?
---------------------------
According to the Official Python Documentation, Name Mangling is designed for two main reasons:
Avoiding Name Clashes: If you have a large inheritance tree (like your Doctor/Employee system), a child class might accidentally use the same variable name as a parent. Mangling ensures they stay separate.
Preventing Accidental Overrides: It protects internal "API" variables from being changed by someone using your class who doesn't realize that variable is critical for the class to function.

3- Comparison of "Privacy" in Python
------------------------------------
[field] means Public and so it open for everyone

[_field] means Protected (by convention) Python won't stop you from accessing it.

[__field]	means Private (by Name Mangling) can accessed only via _Class__field

4- Pro-Tip: When to use "Mangled" vs "Protected"
-----------------------------------------------
Use Protected (_field) 90% of the time. It signals "be careful," but doesn't make inheritance difficult.

Use Mangled (__field) only when you are building a library or a highly sensitive base class where you absolutely want to avoid name collisions in subclasses.
