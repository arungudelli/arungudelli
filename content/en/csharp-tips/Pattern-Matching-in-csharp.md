---
title: "Pattern Matching in C#: A Simple Guide with Real-World Examples"
description: "Exploring the various types of patterns supported in C#, how they work, and when to use them—using clear, real-world examples"
date: "2025-04-10T00:00:00+01:00"
lastmod: "2025-04-10T00:00:00+01:00"
draft: "false"
type: "docs"
images: ["images/pattenmatchingincsharp.png"]
---

C# has evolved significantly over the years, and one of its most powerful features is **pattern matching**. 

Recently, while working on a little side project, I stumbled across this beautiful line of C# code.

```csharp
if (person is not null and { Age: > 18 })
{}
```

It looked sleek. It felt elegant. And honestly—it made me pause.

I had been writing null checks and property accessors in the classic way for years:

```csharp
if (person != null && person.Age > 18)
{}
```

Functional? Yes. Readable? Meh. Safe? Debatable—especially when things get more complex.

So I decided to create a quick YouTube Short about this modern syntax. Just a fun little explainer on how C# now lets you combine null checks and property access in a single, clean condition using pattern matching.

{{< youtube sNh1zM9vrFs >}}


I had no idea that one short video would lead me to explore so much more—and show me just how useful and versatile pattern matching is in today’s C#.

This feature enhances readability, reduces boilerplate code, and allows more expressive logic handling. 

In this article, we’ll explore the various types of patterns supported in C#, how they work, and when to use them—using clear, real-world examples.

## 🌱 It All Started With `is`...

My curiosity was piqued.

I already knew about the basic `is` keyword in C#. You’ve probably seen this a thousand times:

```csharp
if (obj is string s)
{
    Console.WriteLine($"It's a string: {s}");
}
```
What I hadn’t fully appreciated was how the `is` keyword had evolved to handle types, conditions, properties, and even complex object shapes—all in one go.



{{< figure
  src="images/pattenmatchingincsharp.png"
  alt="Pattern Matching in C#"
  caption="Pattern Matching in C#"
>}}

---

## ✨ What is Pattern Matching?

Pattern matching is a mechanism that allows you to compare an input value against a pattern and take action if it matches. In C#, pattern matching is supported in the following constructs:

- `is` expressions  
- `switch` statements  
- `switch` expressions  

C# supports a rich variety of patterns, which we’ll explore one by one.

---

## 🧾 1. Declaration and Type Patterns

These patterns check the runtime type of an object and optionally assign it to a new variable.

**Example:**

```csharp
object item = "Welcome!";
if (item is string text)
{
    Console.WriteLine(text.ToUpper()); // Output: WELCOME!
}
```

Real-world analogy: Imagine a customer is an object. If it's a `PremiumCustomer`, we can cast it and apply special rules.

---

## 🎯 2. Constant Patterns

Use these to compare a value directly with a constant. This is a concise alternative to multiple `if` statements.

**Example:**

```csharp
int guests = 2;
string table = guests switch
{
    1 => "Single Table",
    2 => "Couple Booth",
    4 => "Family Table",
    _ => "Group Table"
};
```

Think of this like a restaurant assigning tables based on the number of people.

---

## 🧮 3. Relational Patterns

These patterns let you check if a value is less than, greater than, or equal to a constant.

**Example:**

```csharp
double temperature = 35.2;

string category = temperature switch
{
    < 0 => "Freezing",
    >= 0 and < 20 => "Cold",
    >= 20 and <= 30 => "Warm",
    > 30 => "Hot",
    _ => "Unknown"
};
```

Great for scenarios like weather categorization or grading systems.

---

## 🔗 4. Logical Patterns

Combine patterns using `and`, `or`, and `not`.

**Example:**

```csharp
int age = 25;
bool isYoungAdult = age is >= 18 and <= 30;
```

Use `not` for exclusions:

```csharp
if (user is not null)
{
    // user is valid
}
```

Logical patterns allow for more complex decision trees with less noise.
---

## 🏠 5. Property Patterns

Match based on values of properties within an object.

**Example:**

```csharp
var booking = new { RoomType = "Suite", Guests = 2 };

if (booking is { RoomType: "Suite", Guests: > 1 })
{
    Console.WriteLine("Apply luxury tax.");
}
```

This is like inspecting a record's fields to decide actions.

---

## 🧭 6. Positional Patterns

Deconstruct objects or tuples to match individual components.

**Example:**

```csharp
(Point x, Point y) = (new(0, 0), new(1, 1));

string status = (x, y) switch
{
    (0, 0) => "At origin",
    (_, _) => "Somewhere else"
};
```

Works great when modeling coordinates, ranges, or grid systems.


👉 **Want to dive deeper into how positional pattern matching works and where it shines?**  
[Read this detailed article on Positional Patterns in C# – The What, Why, and How]({{< relref "csharp-tips/positional-patterns-csharp.md" >}})  

---

## 📦 7. Var Pattern

Use this when you don’t care about the type and just want to extract the value.

**Example:**

```csharp
if (GetData() is var data && data.Length > 0)
{
    Console.WriteLine("Data retrieved!");
}
```

This is handy when performing checks or transformations on the fly.

---

## ⛔ 8. Discard Pattern

Use `_` to match anything when the specific value is irrelevant.

**Example:**

```csharp
string GetDayStatus(DayOfWeek? day) => day switch
{
    DayOfWeek.Monday => "Start of week",
    DayOfWeek.Friday => "Almost weekend",
    _ => "Another day"
};
```

Helpful for catch-all fallbacks.

---

## 📋 9. List Patterns (C# 11+)

Allows checking sequences (like arrays/lists) with nested patterns.

**Example:**

```csharp
int[] ratings = { 5, 4, 3 };

if (ratings is [5, .., >= 3])
{
    Console.WriteLine("Great feedback!");
}
```

You can also extract slices using `..`.

```csharp
if (ratings is [_, .. var middle, _])
{
    Console.WriteLine($"Middle scores: {string.Join(", ", middle)}");
}
```

Useful for validating structured input like exam scores, configuration arrays, etc.

---

## 📚 Summary

| Pattern Type      | Best Use Case |
|------------------|----------------|
| Declaration/Type | Type checking and casting |
| Constant          | Exact value matching |
| Relational        | Range comparison |
| Logical           | Complex combinations |
| Property          | Matching object’s property values |
| Positional        | Matching based on deconstruction |
| Var               | General value extraction |
| Discard           | Match anything, ignore value |
| List              | Matching arrays/lists and subsequences |

---

## 🎯 When Should You Use Pattern Matching?

From my experience, pattern matching shines when:

- You're working with heterogeneous types (e.g. `object` parameters).
- You want to avoid verbose null checks.
- You want to make conditionals more readable.
- You're handling complex branching logic (e.g. transforming API responses).

## 🧠 Final Thoughts

The more I practiced, the more I realized:
Pattern matching in C# isn’t just a syntax trick—it’s a mindset shift.

Instead of writing logic as procedural steps, you describe it as shapes and rules. You tell C# what you expect, and let the compiler do the work.

Whether you’re building parsers, validation logic, or just simplifying conditionals, pattern matching can help you write cleaner and more maintainable code.

Ready to dive deeper? Try refactoring one of your recent switch-heavy or `if`-nested blocks into elegant pattern-based logic.
