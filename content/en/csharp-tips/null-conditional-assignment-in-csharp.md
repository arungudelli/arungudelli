---
title: "💡Null-Conditional Assignment in C# – A Cleaner Way to Handle Nulls in .NET 10"
description: "💡 Null-Conditional Assignment in C# – A Cleaner Way to Handle Nulls in .NET 10"
date: "2025-04-16T00:00:00+01:00"
lastmod: "2025-04-16T00:00:00+01:00"
draft: "false"
type: "docs"
images: ["images/field-keyword.webp"]
---

While working with the latest **.NET 10 Preview 3**, I came across a new language feature in C# 14 that simplifies how we assign values to nullable objects: **null-conditional assignment**.

It’s a small addition, but it helps reduce repetitive null checks and makes your code cleaner. 

Let me show you how it works with a simple example.

---

## 🌱 The Problem: Repetitive Null Checks

```csharp
public class Customer
{
    public string Name { get; set; }
    public int Age { get; set; }
}

public class UpdateCustomer
{
    public static void UpdateAge(Customer? customer, int newAge)
    {
        if (customer is not null)
        {
            customer.Age = newAge;
        }
    }
}
```

This is a perfectly valid approach—but it feels a bit verbose for such a simple task. 

We're just ensuring the object isn’t null before performing an assignment.

---

## ✨ The New Way: Null-Conditional Assignment

```csharp
public static void UpdateAge(Customer? customer, int newAge)
{
    customer?.Age = newAge;
}
```

The `?.` operator ensures that the assignment happens **only if `customer` is not null**. 

If it is null, nothing happens—no exception, no error, just a silent skip.

### ⚠️ Note: This Would Fail in Earlier Versions

If you try to use this syntax in earlier C# versions (prior to C# 14), you’ll get a compiler error like:

```
The left-hand side of an assignment must be a variable, property or indexer
```

That's because `customer?.Age` wasn’t considered a valid assignable target until C# 14.

---

## ✅ What This Means for Your Code

- 🔍 Removes the need for manual null checks  
- 🧼 Makes assignments more concise  
- 🛡️ Protects from `NullReferenceException`  
- 💡 Supported by IDEs (once fully available)

Example use:

```csharp
order?.Status = "Shipped";
user?.LastLogin = DateTime.UtcNow;
config?.RetryCount = 3;
```

---

## 🧪 Real-World Example

```csharp
public void UpdateCustomerInfo(Customer? customer, string? name, int? age)
{
    customer?.Name = name ?? "Unknown";
    if (age.HasValue)
        customer?.Age = age.Value;
}
```

This approach keeps things short, readable, and safe.

---

## ⚙️ How to Try This Feature

### ✅ Install .NET 10 Preview 3

Get the SDK from [.NET Downloads](https://dotnet.microsoft.com/en-us/download/dotnet/10.0).

### ✅ Set the Language Version to Preview

Update your `.csproj`:

```xml
<PropertyGroup>
  <LangVersion>preview</LangVersion>
</PropertyGroup>
```

---

### ⚠️ Not Yet Supported in Visual Studio

As of now, **Visual Studio 2022 v17.14 Preview 2** still shows:

```
The left-hand side of an assignment must be a variable, property or indexer
```

Even with the correct SDK and LangVersion.

---

### ✅ Use the `dotnet` CLI

Instead, build your project using:

```bash
dotnet build
```

This works perfectly with null-conditional assignment using C# 14.

So until Visual Studio catches up with full support in the editor, use the `dotnet` CLI to test it out.

---

## ✍️ Final Thoughts

This small feature reduces code noise, improves clarity, and protects against null reference errors—all while staying elegant.

---

## 📌 TL;DR

- ✅ Introduced in .NET 10 Preview 3  
- ♻️ Assign values only when the object is non-null  
- 🧪 Use `<LangVersion>preview</LangVersion>` in `.csproj`  
- 🧱 Not yet fully supported in Visual Studio  
- ✅ Use `dotnet build` CLI to test