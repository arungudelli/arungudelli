---
title: "Exploring the New 'field' Keyword in C# 14 with .NET 10 Preview 2"
description: "Exploring the New 'field' Keyword in C# 14 with .NET 10 Preview 2"
date: "2025-04-06T00:00:00+01:00"
lastmod: "2025-04-06T00:00:00+01:00"
draft: "false"
type: "docs"
images: ["images/field-keyword.webp"]
---

As someone who's always excited about the latest developments in the .NET ecosystem, I recently got my hands on **.NET 10 Preview 2**, and with it, **C# 14**. 

Among the several new features introduced, one particularly elegant addition stood out to me—the **`field` keyword** for property accessors. 

It's a small addition on the surface, but it has significant implications for cleaner, more expressive code.

In this post, I’ll walk through what the `field` keyword does, how it simplifies property declarations, and some edge cases to be aware of.

{{< youtube 8VRtVux0q5o >}}

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

But what happens when you already have a **local or class-level variable named `field`**, it can create ambiguity.

Let’s explore that with a practical example:

```csharp
internal class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("C# 14 Field Keyword");
    }

    static int field = 3;

    internal class Employee
    {
        public string Name
        {
            get;
            set
            {
                field = value.Length > @field ? value : throw new ArgumentException("Name is too short.");
            }
        }
    }
}
```

If you already have a variable named `field` (like the static variable in the `Program` class), and you also want to use the new contextual `field` keyword within a property, **you must escape your variable name using `@field`**.

This tells the compiler:  
> “Hey, I’m referring to the user-defined variable, not the backing field.”

🧠 **Code Explanation:**

- `static int field = 3;`  
  This defines a static variable named `field` in the outer `Program` class.

- Inside the nested `Employee` class, the `Name` property uses:
  ```csharp
  field = value.Length > @field ? value : throw new ArgumentException(...);
  ```
  - On the **left-hand side**, `field =` refers to the **compiler-generated backing field** for the `Name` property. This is a new feature introduced in C# 14.
  - On the **right-hand side**, `@field` refers to our static variable from the outer `Program` class.

So the logic here checks:
- If the incoming `value` (i.e., the name being set) is longer than 3 characters (`@field` = 3),
- Then it gets assigned to the backing field via the new `field` keyword,
- Otherwise, it throws an exception.

If you try to assign a name with more than 3 characters — say `"John"` — it will be accepted. Anything shorter, like `"Al"`, will raise an error:

```
ArgumentException: Name is too short.
```

Let’s take another example — this time, we have a **class-level field** named `field`.

```csharp
public class Person
{
    private int field = 18;

    public int Age
    {
        get;
        set => field = value > this.field ? value : throw new ArgumentException("Age must be higher than the existing field.");
    }
}
```

🧠 **Code Explanation:**

- `this.field` refers to the **class-level variable** holding the value `18`.
- `field =` on the left side refers to the **auto-generated backing field** of the `Age` property.

So this line of code means:  

👉 Assign the new value to the property **only if it's greater than the existing `field` variable**.

By using `this.field`, you're making it crystal clear that you're talking about the class-level variable — which avoids confusion with the compiler’s contextual `field`. 

Or you can use `@field` also.



🧠 **Tip:** When dealing with properties using the `field` keyword, it’s best to avoid naming other variables `field`. 

If necessary, you can use `@field` to refer local variable and `this.field` or `@field` to reference class level fields.

Let `field` (without `@`) refer to the auto-property backing field.

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











