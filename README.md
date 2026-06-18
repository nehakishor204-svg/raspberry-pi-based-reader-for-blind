# Raspberry Pi Based Reader for the Blind

Mini-project (APJ Abdul Kalam Technological University) — co-developed with a 4-member team at Government Engineering College Wayanad.

## Overview
An assistive device that converts printed text into speech in real time, helping visually impaired users read books, documents, and labels independently. Built using a Raspberry Pi 5, Pi Camera, Optical Character Recognition (OCR), and a Text-to-Speech (TTS) engine.

## Problem
Visually impaired individuals face significant barriers accessing printed text. Braille requires specialized training and materials, and existing screen readers don't work with physical printed documents. This project provides an affordable, portable, real-time solution.

## System Architecture
- **Pi Camera** captures an image of printed text on button press
- **Raspberry Pi 5** processes the image using Tesseract OCR to extract text
- Extracted text is converted to speech using a TTS engine
- Audio output is delivered through a connected speaker

## Approach
1. Image Capturing — Pi Camera captures the document on push-button trigger
2. Image Preprocessing — prepares the image for accurate OCR
3. Text Extraction — Tesseract OCR converts image to machine-readable text
4. Text-to-Speech Conversion — extracted text converted to audible speech
5. Speech Output — delivered via speaker in real time

## Hardware
Raspberry Pi 5 (4GB), Pi Camera (5MP), Speaker (3.5mm AUX), Push Button (x2), Power Supply

## Software
Python, Tesseract OCR (pytesseract), Text-to-Speech engine, EasyEDA (circuit design)

## Results
Successfully converts printed text to speech in real time under good lighting conditions with clear print. Performs reliably for books, documents, and labels — though accuracy decreases with handwritten text, poor print quality, or challenging lighting.

## My Contribution
Contributed to image processing, OCR pipeline implementation, system testing and TTS Implementation.

## Team
Neha Kishor, Keerthana Prasad, Jilna KJ, Muhammed Fuad Saneen
Government Engineering College Wayanad, 2024-25

## Future Scope
AI-based OCR for improved accuracy, multilingual support, enhanced natural-sounding TTS voices, mobile app integration.
