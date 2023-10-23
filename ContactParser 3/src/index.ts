import { parseContacts } from "./contactParser";

// Example usage
const importedContacts = [
  {
    name: "John Doe",
    email: "johndoe@example.com",
    phone: "1234567890",
  },
  {
    name: "Jane Smith",
    email: "janesmith@example.com",
    phone: "9876543210",
  },
];

const parsedContacts = parseContacts(importedContacts);
console.log(parsedContacts);