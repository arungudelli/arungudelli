---
title: "Positional Patterns in C#: The What, Why, and How"
description: "What positional patterns are, when to use them, and how they compare to other matching techniques like property patterns"
date: "2025-04-16T00:00:00+01:00"
lastmod: "2025-04-16T00:00:00+01:00"
draft: "false"
type: "docs"
images: ["images/Positional-Patterns-in-Csharp.png"]
---

C# has been evolving steadily, and with C# 8.0 and beyond, pattern matching got a serious power-up. 

One of the coolest additions is **Positional Patterns**. 

If you've ever written code that checks for multiple values inside a class or struct, this feature might just make your code cleaner and easier to read.

In this post, let me walk you through what positional patterns are, when to use them, and how they compare to other matching techniques like property patterns.

{{< figure
  process="fill 2100x900"
  lqip="21x webp q20"
  loading="lazy"
  fetchpriority="auto" 
  sizes="auto"
  src="images/Positional-Patterns-in-Csharp.png"
  alt="Positional Patterns in C#"
  caption="Positional Patterns in C#"
>}}

---

## 🚀 What Are Positional Patterns?

Positional patterns allow you to **deconstruct** an object and **match** its components based on position (not property names). 

They're super handy for checking specific values or shapes of objects in a concise way.

### 🔧 But Here's the Catch:

You **must** define a `Deconstruct()` method in your class or struct. 

This method tells the compiler how to break your object down into pieces (positions).

---

## 🧪 Example: Matching a Point on the Axis

```csharp
public class Point
{
    public int X { get; }
    public int Y { get; }

    public Point(int x, int y) => (X, Y) = (x, y);

    public void Deconstruct(out int x, out int y)
    {
        x = X;
        y = Y;
    }
}
```

Now we can use positional patterns:

```csharp
var point = new Point(0, 5);

if (point is (0, _))
    Console.WriteLine("Point lies on the Y axis");
else if (point is (_, 0))
    Console.WriteLine("Point lies on the X axis");
```

Here, `(0, _)` and `(_, 0)` are positional patterns. You’re matching the shape of the `Point` object.

---

## 🔁 With switch Statement

```csharp
switch (point)
{
    case (0, 0):
        Console.WriteLine("Origin");
        break;
    case (0, _):
        Console.WriteLine("Y Axis");
        break;
    case (_, 0):
        Console.WriteLine("X Axis");
        break;
    default:
        Console.WriteLine("Somewhere else");
        break;
}
```

---

## ❌ What If You Don't Have a Deconstruct Method?

If `Deconstruct()` is not defined, you'll get an error like:

> CS8129: No suitable 'Deconstruct' instance or extension method was found...

But don't worry — you can use **property patterns** instead!

### ✅ Property Pattern Alternative

```csharp
public class Point
{
    public int X { get; set; }
    public int Y { get; set; }
}

if (point is { X: 0, Y: 0 })
    Console.WriteLine("Origin");
```

Much cleaner than nested `if` conditions, and **no Deconstruct needed**.

---

## 🆚 Positional vs Property Patterns

| Pattern Type         | Needs `Deconstruct()` | Syntax Example       |
|----------------------|-----------------------|----------------------|
| Positional Pattern   | ✅ Yes                | `is (0, _)`          |
| Property Pattern     | ❌ No                 | `is { X: 0, Y: _ }`  |

Both are useful — choose based on your use case.

---

## 🧠 Summary

- Positional patterns are great for short, clean matching logic.
- You need to implement a `Deconstruct()` method.
- If that’s not feasible, property patterns are your friend.
- Combine with `switch` for readable, declarative matching.

---

C# pattern matching just keeps getting better, and positional patterns make it easier to write expressive and elegant code. 

Try adding a `Deconstruct()` method to your classes and see how it changes your matching logic.

Have you tried using positional patterns in your code yet? If not, give it a shot in your next project! ✨