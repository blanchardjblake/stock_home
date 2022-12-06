const profile_number = Math.floor(100000 * Math.random());
const test_user = `test_user_${profile_number}@test.com`;
const test_password = 'T35t1234';

describe('Create User', () => {
    it('Should create a test user.', () => {
        cy.visit('accounts/signup/');
        cy.get('input[id="id_first_name"]').type('Test');
        cy.get('input[id="id_last_name"]').type('User');
        cy.get('input[id="id_email"]').type(test_user);
        cy.get('input[id="id_password1"]').type(test_password);
        cy.get('input[id="id_password2"]').type(test_password);
        cy.get('form').submit();
    });
});

describe('Access Company Create Non Admin', () => {
    beforeEach(() => {
        cy.login(test_user, test_password);
    });
    it('Should redirect to list page.', () => {
        cy.visit('stock_home/company/create/');
        cy.getCookies()
            .should('have.length', 2)
            .then((cookies) => {
                expect(cookies[0]).to.have.property('name', 'sessionid');
            });
        cy.url().should('contain', 'stock_home/company');
        cy.contains(test_user); // If this fails, Cypress is logging the user out too early
    });
});

describe('Access Company Delete Non Admin', () => {
    beforeEach(() => {
        cy.login(test_user, test_password);
        cy.visit('stock_home/company/1/delete/');
    });
    it('Should redirect to list page.', () => {
        cy.url().should('contain', 'stock_home/company');
    });
});

describe('Access Company Update Non Admin', () => {
    beforeEach(() => {
        cy.login(test_user, test_password);
    });
    it('Should redirect to list page.', () => {
        cy.visit('stock_home/company/1/update/');
        cy.url().should('contain', 'stock_home/company');
    });
});

describe('Transaction List no User', () => {
    it('Should redirect to login.', () => {
        cy.visit('stock_home/transactions');
        cy.contains('Please login to see this page.');
    });
});

describe('Transaction Create', () => {
    beforeEach(() => {
        cy.login(test_user, test_password);
    });
    it('Should create a transaction.', () => {
        cy.visit('stock_home/transactions/create/');
        cy.get('select[name="company"]').select('1');
        cy.get('input[name="quantity"]').click();
        for (let i = 0; i < 3; i++) cy.get('input[name="quantity"]').type('{backspace}');
        cy.get('input[name="quantity"]').type('5.0');
        cy.get('input[name="price"]').click();
        for (let i = 0; i < 3; i++) cy.get('input[name="price"]').type('{backspace}');
        cy.get('input[name="price"]').type('5.0');
        cy.get('form').submit();
        cy.url().should('contain', 'stock_home/transactions');
    });
});

describe('Transaction View', () => {
    beforeEach(() => {
        cy.login(test_user, test_password);
    });
    it('Should view a transaction for the current user.', () => {
        cy.visit('stock_home/transactions');
        cy.get('a[class="transaction_li"]').click();
        cy.contains('User:');
        cy.contains('Company:');
        cy.contains('Type:');
    });
});