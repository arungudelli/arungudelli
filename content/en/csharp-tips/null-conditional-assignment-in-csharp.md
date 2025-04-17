---
title: "💡Null-Conditional Assignment in C# – A Cleaner Way to Handle Nulls in .NET 10"
description: "💡 Null-Conditional Assignment in C# – A Cleaner Way to Handle Nulls in .NET 10"
date: "2025-04-16T00:00:00+01:00"
lastmod: "2025-04-16T00:00:00+01:00"
draft: "false"
type: "docs"
images: ["images/null-conditional-assignment-csharp.png"]
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

{{< figure
  process="fill 2100x900"
  lqip="21x webp q20"
  loading="lazy"
  fetchpriority="auto" 
  sizes="auto"
  src="images/null-conditional-assignment-csharp.png"
  alt="Null-Conditional Assignment C#"
  caption="Null-Conditional Assignment C#"
>}}

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

Let’s simulate a practical use case: an application receives optional user profile data from an API, and we want to update it only if the data exists.

### 🧱 Supporting Classes: `UserProfile` and `ProfileService`

```csharp
using System;

namespace NullConditionalAssignmentDemo
{
    public class UserProfile
    {
        public string? DisplayName { get; set; }
        public string? Bio { get; set; }
        public int Age { get; set; }

        public void Print()
        {
            Console.WriteLine($"DisplayName: {DisplayName ?? "N/A"}");
            Console.WriteLine($"Bio: {Bio ?? "N/A"}");
            Console.WriteLine($"Age: {Age}");
        }
    }

    public class ProfileService
    {
        public UserProfile? GetProfileFromApi(string username)
        {
            if (username.ToLower() == "ghost") return null;

            return new UserProfile
            {
                DisplayName = "Arun Gudelli",
                Bio = "C# Developer | Tech Blogger",
                Age = 29
            };
        }

        public void UpdateProfile(UserProfile? profile, string? newBio, int? newAge)
        {
            profile?.Bio = newBio;
            if (newAge.HasValue)
                profile?.Age = newAge.Value;
        }
    }
}
```

**Explanation:**
- `UserProfile` is a basic data model class with nullable properties and a `Print()` method for displaying values.
- `ProfileService` simulates external API behavior. If the input is `"ghost"`, it returns `null`, representing a failed or empty response.
- The `UpdateProfile` method uses null-conditional assignment to update the profile safely, without any `if (profile != null)` checks.

One important takeaway here is that we can still safely call `UpdateProfile` even if the profile is `null`.

Normally, this might lead to a `NullReferenceException`, but thanks to **null-conditional assignment**, the assignments are silently skipped if the object is `null`.

In the `UpdateProfile` method, we use statements like `profile?.Bio = newBio` which ensures that the assignment only occurs if profile is not `null`.

Even if the caller passes a `null` profile (like when the `user` is `ghost`), the method runs without any exceptions.

The same goes for age—if we have a non-null value (`int?`), we assign it to `profile?.Age = newAge.Value`, which again runs only if the profile is not `null`.

This design pattern simplifies calling logic—no need to check for null before every update. 

The update method itself safely handles it, keeping the code both neat and expressive.

---

### 🚀 Main Program: Using the Classes with Null-Safe Updates

```csharp
using System;

namespace NullConditionalAssignmentDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            var service = new ProfileService();

            string username1 = "arun";
            string username2 = "ghost";

            var profile1 = service.GetProfileFromApi(username1);
            var profile2 = service.GetProfileFromApi(username2);

            string? updatedBio = "Updated bio from UI";
            int? updatedAge = 30;

            service.UpdateProfile(profile1, updatedBio, updatedAge);
            service.UpdateProfile(profile2, updatedBio, updatedAge);

            Console.WriteLine("Profile 1 (arun):");
            profile1?.Print();

            Console.WriteLine("Profile 2 (ghost):");
            profile2?.Print();
        }
    }
}
```
**Explanation:**

- In this main program, we simulate two scenarios:
  - One where a valid profile is returned (`arun`)
  - Another where the user does not exist and the method returns `null` (`ghost`)
- Both profiles are passed to the `UpdateProfile` method.
- The method contains null-conditional assignments like `profile?.Bio = newBio`, which means the update only happens if the profile is not null.
- Even if `profile` is `null`, the method executes safely without throwing any exception.
- This eliminates the need for the caller to check if the object is null before calling the method.
- Finally, we use `profile?.Print()` to display the result. For `arun`, it prints the updated profile. For `ghost`, nothing is printed, but no error is thrown.
- This demonstrates how null-conditional access and assignment provide safe and readable ways to deal with possibly-null objects.

**Output**:

```
Profile 1 (arun):
DisplayName: Arun Gudelli
Bio: Updated bio from UI
Age: 30
Profile 2 (ghost):
```

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
- 🔁 Assign values only when the object is non-null  
- 🧪 Use `<LangVersion>preview</LangVersion>` in `.csproj`  
- 🧱 Not yet fully supported in Visual Studio  
- ✅ Use `dotnet build` CLI to test






