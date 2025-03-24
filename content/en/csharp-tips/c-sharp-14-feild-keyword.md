---
title: "Exploring the New 'field' Keyword in C# 14 with .NET 10 Preview 2"
description: "Exploring the New 'field' Keyword in C# 14 with .NET 10 Preview 2"
date: "2025-03-23T00:00:00+01:00"
lastmod: "2025-03-23T00:00:00+01:00"
draft: "false"
type: "docs"
images: ["images/field-keyword.webp"]
---

As someone who's always excited about the latest developments in the .NET ecosystem, I recently got my hands on **.NET 10 Preview 2**, and with it, **C# 14**. 

Among the several new features introduced, one particularly elegant addition stood out to me—the **`field` keyword** for property accessors. 

It's a small addition on the surface, but it has significant implications for cleaner, more expressive code.

In this post, I’ll walk through what the `field` keyword does, how it simplifies property declarations, and some edge cases to be aware of.



---

## The Problem with Traditional Property Backing Fields

Before C# 14, if you wanted to perform logic inside a property accessor—like validating input—you had to manually declare a **backing field**. Here’s a typical example where we ensure a string property can't be set to `null`:

```csharp
private string _message;

public string Message
{
    get => _message;
    set => _message = value ?? throw new ArgumentNullException(nameof(value));
}
```

This works fine, but it's verbose. You end up duplicating property and field names, and it breaks the neatness of auto-properties.

---

## The Solution: Enter the `field` Keyword

C# 14 introduces a new contextual keyword called `field`, which allows us to **directly access the compiler-generated backing field** of an auto-property inside the accessor logic.

Here's how the previous code looks using the new `field` keyword:

```csharp
public string Message
{
    get;
    set => field = value ?? throw new ArgumentNullException(nameof(value));
}
```

✨ Much cleaner, right?

You get the benefit of auto-properties *and* the ability to add logic, all without manually declaring a backing field.

---

## How It Works

- `field` is a **contextual keyword**, meaning it only has special meaning **inside property accessors**.
- It references the compiler-generated backing field that underlies an auto-property.
- You can use `field` in `get` or `set`, or both, depending on your logic needs.

Example with both:

```csharp
public int Age
{
    get => field;
    set => field = value > 0 ? value : throw new ArgumentOutOfRangeException(nameof(value));
}
```

---

## When Should You Use `field`?

Use the `field` keyword when:

- You want to add simple logic (validation, transformation) in an accessor.
- You don't want to manually manage a backing field.
- You want your property declarations to remain compact and readable.

This change encourages better encapsulation and makes it easier to refactor.

---

## Disambiguation: What if You Already Have a Variable Named `field`?

Since `field` is a **contextual keyword**, it only has special meaning inside property accessors. 

But if you already have a **local or class-level variable named `field`**, it can create ambiguity.

If you have such a symbol within the same scope, you can resolve conflicts by:

- Using `@field` to refer to the symbol

```csharp
string field = "local";
public string Name
{
    get => @field; // refers to the local variable, not the compiler field
    set => field = value; // this would be ambiguous
}
```
- Using `this.field` for class-level fields.

Here's an example:

```csharp
int field = 18;

/// <summary>
/// Age must be greater than 18
/// </summary>
public int Age
{
    get;
    set => field = value > @field ? value : throw new ArgumentNullException(nameof(value));
}
```

In this case:
- The local variable `int field = 18;` shadows the contextual `field` keyword.
- Inside the property:
  - `@field` refers explicitly to the **local variable** named `field`.
  - `field = value` refers to the **compiler-generated backing field** for the `Age` property.

This ensures that the property only allows values **greater than 18**, where `18` is held in the local variable.

🧠 **Tip:** When dealing with properties using the `field` keyword, it’s best to avoid naming other variables `field`. 

If necessary, you can use `@field` or `this.field` to reference your own variable and let `field` (without `@`) refer to the auto-property backing field.

---

## Limitations and Notes

- This feature is only available starting with **C# 14**, which you can try by installing **.NET 10 Preview 2** and setting your `LangVersion` to `preview`.
- The compiler only synthesizes a backing field if both accessors (`get`/`set`) do not contain logic that prevents auto-property generation (e.g., referencing external members).
- Not suitable for complex getter logic or if you want custom fields unrelated to properties.

---

## Getting Started with C# 14 and .NET 10 Preview 2

To test this out:

1. Install [.NET 10 Preview 2 SDK](https://dotnet.microsoft.com/en-us/download/dotnet/10.0).
2. Create a new project:
   ```bash
   dotnet new console -n CSharp14FieldDemo
   cd CSharp14FieldDemo
   ```
3. Edit your `.csproj` to use the preview language features:
   ```xml
   <PropertyGroup>
     <LangVersion>preview</LangVersion>
   </PropertyGroup>
   ```
4. Write your code and explore!

---

## Final Thoughts

The introduction of the `field` keyword may seem like a minor syntactic sugar at first glance, but it reinforces C#’s philosophy of **clear, concise, and expressive code**. It strikes a nice balance between automation and control, giving you just enough power without the boilerplate.

If you’re already testing out .NET 10, I highly recommend trying this feature—it’s a subtle but satisfying upgrade.

Happy coding! 👨‍💻🚀











