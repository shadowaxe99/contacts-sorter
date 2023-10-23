import { expect } from 'chai';
import { parseContact } from '../src/contactParser';

describe('Contact Parser', () => {
  it('should parse imported contacts and extract relevant information', () => {
    const importedContact = {
      name: 'John Doe',
      email: 'johndoe@example.com',
      phone: '1234567890',
      address: '123 Main St',
    };

    const parsedContact = parseContact(importedContact);

    expect(parsedContact.name).to.equal('John Doe');
    expect(parsedContact.email).to.equal('johndoe@example.com');
    expect(parsedContact.phone).to.equal('1234567890');
    expect(parsedContact.address).to.equal('123 Main St');
  });
});
