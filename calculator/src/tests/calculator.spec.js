import { test, expect } from '@playwright/test';

test.describe('React Calculator App', () => {
    test.beforeEach(async ({ page }) => {
        await page.goto('http://localhost:5173'); // Adjust if your dev server runs on a different port
    });

    test('Addition works correctly', async ({ page }) => {
        await page.locator('input[name="number1"]').fill('10');
        await page.locator('input[name="number2"]').fill('5');
        await page.locator('button', { hasText: '+' }).click();
        await expect(page.locator('h1')).toHaveText('15');
    });

    test('Subtraction works correctly', async ({ page }) => {
        await page.locator('input[name="number1"]').fill('10');
        await page.locator('input[name="number2"]').fill('5');
        await page.locator('button', { hasText: '-' }).click();
        await expect(page.locator('h1')).toHaveText('5');
    });

    test('Multiplication works correctly', async ({ page }) => {
        await page.locator('input[name="number1"]').fill('10');
        await page.locator('input[name="number2"]').fill('5');
        await page.locator('button', { hasText: '*' }).click();
        await expect(page.locator('h1')).toHaveText('50');
    });

    test('Division works correctly', async ({ page }) => {
        await page.locator('input[name="number1"]').fill('10');
        await page.locator('input[name="number2"]').fill('5');
        await page.locator('button', { hasText: '/' }).click();
        await expect(page.locator('h1')).toHaveText('2');
    });
});