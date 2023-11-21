
# Class-Gen-Assistant

This tool converts input text data to .NET C# plain old class object (POCO)

## Text Input descriptor format for a C# POCO class

## Standard Format

### Class Name Declaration:  

Format: ClassName: [Name]  
Example: ClassName: Person  

### Property Specification:

Each property on a new line.  
Types should be valid C# types (e.g., int, string, DateTime).  

Format: [Type] [PropertyName]  

Example:  
string Name  
int Age  
DateTime BirthDate  

### Optional Attributes:

Attributes can be added in parentheses after the property.  

Format: [Type] [PropertyName] ([Attribute1, Attribute2, ...])  
Example: string Name (Required, MaxLength(50))  
Comments:  

Start with // and add at the end of any line.  
Example: int Age // Age of the person  

### Example Input  

ClassName: Person  
string Name (Required, MaxLength(50))  
int Age // Age of the person  
DateTime BirthDate  