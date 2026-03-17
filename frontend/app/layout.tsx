import './globals.css';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Cortex — Autonomous AI Workforce',
  description: 'Your AI Workforce That Actually Works'
};

export default function RootLayout({
  children
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
