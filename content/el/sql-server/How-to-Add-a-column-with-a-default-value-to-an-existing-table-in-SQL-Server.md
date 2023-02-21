---
title: "Πώς να προσθέσετε μια στήλη με προεπιλεγμένη τιμή σε έναν υπάρχοντα πίνακα στον SQL Server"
description: "Στον SQL server, για να προσθέσετε μια στήλη με προεπιλεγμένη τιμή σε έναν υπάρχοντα πίνακα χρησιμοποιήστε τον πίνακα 'ALTER' 'ADD' όνομα στήλης με περιορισμό 'NULL/NOT NULL' με τιμή 'DEFAULT'."
date: 2023-02-20T14:41:21+01:00
lastmod: 2023-02-20T14:41:21+01:00
contributors: ["Arun Gudelli"]
draft: false
images: []
type: docs
---

Στον SQL server, Για να προσθέσετε μια στήλη με προεπιλεγμένη τιμή σε έναν υπάρχοντα πίνακα χρησιμοποιήστε τον πίνακα `ALTER` Πίνακας `ADD` Όνομα στήλης με περιορισμό `NULL/NOT NULL` με τιμή `DEFAULT`.

Η παρακάτω σύνταξη ερωτήματος του sql server μπορεί να χρησιμοποιηθεί για την προσθήκη μιας στήλης με προεπιλεγμένη τιμή στον υπάρχοντα πίνακα.

```sql
ALTER TABLE {TABLENAME} 
ADD {COLUMNNAME} {TYPE} {NULL|NOT NULL} 
CONSTRAINT {CONSTRAINT_NAME} DEFAULT {DEFAULT_VALUE}
WITH VALUES
```

Ας δούμε ένα παράδειγμα για να το κατανοήσουμε καλύτερα.

## Προσθήκη μιας μη μηδενικής στήλης με προεπιλεγμένη τιμή για τις υπάρχουσες εγγραφές

Θεωρήστε έναν πίνακα `Employee` στον SQL server και αν θέλουμε να προσθέσουμε τη στήλη ελάχιστος μισθός με προεπιλεγμένη τιμή `1000USD`, χρησιμοποιήστε το παρακάτω ερώτημα.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL DEFAULT(1000)
GO
```

Το παραπάνω ερώτημα θα προσθέσει μια νέα στήλη `MINIMUM_WAGE` στον πίνακα `Employee` και θα γεμίσει τη στήλη στις υπάρχουσες γραμμές με την προεπιλεγμένη τιμή, δηλαδή `1000`. 

Επειδή έχουμε προσθέσει τον περιορισμό `NOT NULL`.

Εάν δεν προσθέσετε τον περιορισμό `NOT NULL`, όλες οι υπάρχουσες γραμμές θα είναι `NULL` και η τιμή `DEFAULT` που παρέχεται δεν θα έχει καμία επίπτωση. 

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int DEFAULT(1000)
GO
```

Όλες οι τιμές της στήλης `MINIMUM_WAGE` θα είναι `NULL`.

Θα πρέπει να προσθέσετε την τιμή `DEFAULT` αν προσθέσετε τον περιορισμό `NOT NULL` αν ο πίνακας δεν είναι άδειος. 

Για παράδειγμα, αν ο πίνακας `Employee` δεν είναι άδειος και αν προσθέσετε μια νέα στήλη με τον περιορισμό `NOT NULL`, θα εμφανιστεί σφάλμα.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE int NOT NULL
GO
```

Το παραπάνω ερώτημα του sql server θα εμφανίσει το παρακάτω σφάλμα κατά την προσθήκη νέας στήλης στον υπάρχοντα πίνακα.

```text
ALTER TABLE only allows columns to be added that can contain nulls, or have a DEFAULT definition specified, or the column being added is an identity or timestamp column, or alternatively if none of the previous conditions are satisfied the table must be empty to allow addition of this column. Column 'MINIMUM_WAGE' cannot be added to non-empty table 'Employee' because it does not satisfy these conditions.
```

Εάν ο πίνακας `Employee` είναι άδειος. 

Το παραπάνω ερώτημα του sql server θα προσθέσει μια νέα στήλη χωρίς προβλήματα.

## Προσθήκη μηδενιζόμενης στήλης με προεπιλεγμένη τιμή για υπάρχουσες εγγραφές

Εάν θέλετε να προσθέσετε μια nullable στήλη με προεπιλεγμένη τιμή για υπάρχουσες εγγραφές, πρέπει να χρησιμοποιήσετε το `WITH VALUES` στην εντολή sql.

```sql
ALTER TABLE Employee
ADD MINIMUM_WAGE INT
CONSTRAINT Minimum_Pay DEFAULT 1000 WITH VALUES
```

Το παραπάνω ερώτημα θα προσθέσει μια nullable στήλη στον πίνακα του sql server με την προεπιλεγμένη τιμή για τις υπάρχουσες εγγραφές.

Σε αυτό το σεμινάριο μάθαμε να προσθέτουμε μια στήλη, τόσο μηδενική όσο και μηδενική, στον πίνακα του sql server με προεπιλεγμένη τιμή για όλες τις υπάρχουσες εγγραφές.

