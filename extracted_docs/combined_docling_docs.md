# Docling Documentation - Combined Extract

This file contains the combined extracted content from Docling documentation.

## Content from: https://pkg.go.dev/github.com/pdfcpu/pdfcpu/pkg/api

# api

package

[Version: v0.11.0](?tab=versions)

Opens a new window with list of versions in this module.

Latest

Latest

Warning

<!-- image -->

This package is not in the latest version of its module.

[Go to latest](/github.com/pdfcpu/pdfcpu/pkg/api)

Published: May 28, 2025

License: [Apache-2.0](/github.com/pdfcpu/pdfcpu/pkg/api?tab=licenses)

Opens a new window with license information.

[Imports: 27](/github.com/pdfcpu/pdfcpu/pkg/api?tab=imports)

Opens a new window with list of imports.

[Imported by: 230](/github.com/pdfcpu/pdfcpu/pkg/api?tab=importedby)

Opens a new window with list of known importers.

Main

Versions

Licenses

Imports

Imported By

## Details

- Valid [go.mod](https://github.com/pdfcpu/pdfcpu/tree/v0.11.0/go.mod) file The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go.
checked

<!-- image -->
<!-- image -->
- Redistributable license Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed.
checked

<!-- image -->
<!-- image -->
- Tagged version Modules with tagged versions give importers more predictable builds.
checked

<!-- image -->
<!-- image -->
- Stable version When a project reaches major version v1 it is considered stable.
unchecked

<!-- image -->
<!-- image -->
- [Learn more about best practices](/about#best-practices)

## Repository

[github.com/pdfcpu/pdfcpu](https://github.com/pdfcpu/pdfcpu)

## Links

- [Open Source Insights](https://deps.dev/go/github.com%2Fpdfcpu%2Fpdfcpu/v0.11.0)
Image Hyperlink.

<!-- image -->

Jump to ...

- [Documentation](#section-documentation)
    - [Overview](#pkg-overview)
    - [Index](#pkg-index)
        - [Examples](#pkg-examples)
    - [Constants](#pkg-constants)
    - [Variables](#pkg-variables)
    - [Functions](#pkg-functions)
        - [AddAnnotations(rs, w, selectedPages, ann, conf)](#AddAnnotations)
        - [AddAnnotationsAsIncrement(rws, selectedPages, ar, conf)](#AddAnnotationsAsIncrement)
        - [AddAnnotationsFile(inFile, outFile, selectedPages, ar, conf, incr)](#AddAnnotationsFile)
        - [AddAnnotationsMap(rs, w, m, conf)](#AddAnnotationsMap)
        - [AddAnnotationsMapAsIncrement(rws, m, conf)](#AddAnnotationsMapAsIncrement)
        - [AddAnnotationsMapFile(inFile, outFile, m, conf, incr)](#AddAnnotationsMapFile)
        - [AddAttachments(rs, w, files, coll, conf)](#AddAttachments)
        - [AddAttachmentsFile(inFile, outFile, files, coll, conf)](#AddAttachmentsFile)
        - [AddBookmarks(rs, w, bms, replace, conf)](#AddBookmarks)
        - [AddBookmarksFile(inFile, outFile, bms, replace, conf)](#AddBookmarksFile)
        - [AddBoxes(rs, w, selectedPages, pb, conf)](#AddBoxes)
        - [AddBoxesFile(inFile, outFile, selectedPages, pb, conf)](#AddBoxesFile)
        - [AddImageWatermarksFile(inFile, outFile, selectedPages, onTop, fileName, desc, conf)](#AddImageWatermarksFile)
        - [AddImageWatermarksForReaderFile(inFile, outFile, selectedPages, onTop, r, desc, conf)](#AddImageWatermarksForReaderFile)
        - [AddKeywords(rs, w, files, conf)](#AddKeywords)
        - [AddKeywordsFile(inFile, outFile, files, conf)](#AddKeywordsFile)
        - [AddPDFWatermarksFile(inFile, outFile, selectedPages, onTop, fileName, desc, conf)](#AddPDFWatermarksFile)
        - [AddProperties(rs, w, properties, conf)](#AddProperties)
        - [AddPropertiesFile(inFile, outFile, properties, conf)](#AddPropertiesFile)
        - [AddTextWatermarksFile(inFile, outFile, selectedPages, onTop, text, desc, conf)](#AddTextWatermarksFile)
        - [AddWatermarks(rs, w, selectedPages, wm, conf)](#AddWatermarks)
        - [AddWatermarksFile(inFile, outFile, selectedPages, wm, conf)](#AddWatermarksFile)
        - [AddWatermarksMap(rs, w, m, conf)](#AddWatermarksMap)
        - [AddWatermarksMapFile(inFile, outFile, m, conf)](#AddWatermarksMapFile)
        - [AddWatermarksSliceMap(rs, w, m, conf)](#AddWatermarksSliceMap)
        - [AddWatermarksSliceMapFile(inFile, outFile, m, conf)](#AddWatermarksSliceMapFile)
        - [Annotations(rs, selectedPages, conf)](#Annotations)
        - [Attachments(rs, conf)](#Attachments)
        - [Booklet(rs, w, imgFiles, selectedPages, nup, conf)](#Booklet)
        - [BookletFile(inFiles, outFile, selectedPages, nup, conf)](#BookletFile)
        - [BookletFromImages(conf, imageFileNames, nup)](#BookletFromImages)
        - [Bookmarks(rs, conf)](#Bookmarks)
        - [Box(s, u)](#Box)
        - [Boxes(rs, selectedPages, conf)](#Boxes)
        - [ChangeOwnerPassword(rs, w, pwOld, pwNew, conf)](#ChangeOwnerPassword)
        - [ChangeOwnerPasswordFile(inFile, outFile, pwOld, pwNew, conf)](#ChangeOwnerPasswordFile)
        - [ChangeUserPassword(rs, w, pwOld, pwNew, conf)](#ChangeUserPassword)
        - [ChangeUserPasswordFile(inFile, outFile, pwOld, pwNew, conf)](#ChangeUserPasswordFile)
        - [Collect(rs, w, selectedPages, conf)](#Collect)
        - [CollectFile(inFile, outFile, selectedPages, conf)](#CollectFile)
        - [Create(rs, rd, w, conf)](#Create)
        - [CreateCheatSheetsUserFonts(fontNames)](#CreateCheatSheetsUserFonts)
        - [CreateFile(inFilePDF, inFileJSON, outFilePDF, conf)](#CreateFile)
        - [CreatePDFFile(xRefTable, outFile, conf)](#CreatePDFFile)
        - [CreateUserFontDemoFiles(dir, fn)](#CreateUserFontDemoFiles)
        - [Crop(rs, w, selectedPages, b, conf)](#Crop)
        - [CropFile(inFile, outFile, selectedPages, b, conf)](#CropFile)
        - [Cut(rs, outDir, fileName, selectedPages, cut, conf)](#Cut)
        - [CutFile(inFile, outDir, outFile, selectedPages, cut, conf)](#CutFile)
        - [Decrypt(rs, w, conf)](#Decrypt)
        - [DecryptFile(inFile, outFile, conf)](#DecryptFile)
        - [DisableConfigDir()](#DisableConfigDir)
        - [DumpObject(rs, mode, objNr, conf)](#DumpObject)
        - [DumpObjectFile(inFile, mode, objNr, conf)](#DumpObjectFile)
        - [Encrypt(rs, w, conf)](#Encrypt)
        - [EncryptFile(inFile, outFile, conf)](#EncryptFile)
        - [EnsureDefaultConfigAt(path)](#EnsureDefaultConfigAt)
        - [ExportBookmarksFile(inFilePDF, outFileJSON, conf)](#ExportBookmarksFile)
        - [ExportBookmarksJSON(rs, w, source, conf)](#ExportBookmarksJSON)
        - [ExportForm(rs, source, conf)](#ExportForm)
        - [ExportFormFile(inFilePDF, outFileJSON, conf)](#ExportFormFile)
        - [ExportFormJSON(rs, w, source, conf)](#ExportFormJSON)
        - [ExtractAttachments(rs, outDir, fileNames, conf)](#ExtractAttachments)
        - [ExtractAttachmentsFile(inFile, outDir, files, conf)](#ExtractAttachmentsFile)
        - [ExtractAttachmentsRaw(rs, outDir, fileNames, conf)](#ExtractAttachmentsRaw)
        - [ExtractContent(rs, outDir, fileName, selectedPages, conf)](#ExtractContent)
        - [ExtractContentFile(inFile, outDir, selectedPages, conf)](#ExtractContentFile)
        - [ExtractFonts(rs, outDir, fileName, selectedPages, conf)](#ExtractFonts)
        - [ExtractFontsFile(inFile, outDir, selectedPages, conf)](#ExtractFontsFile)
        - [ExtractImages(rs, selectedPages, digestImage, conf)](#ExtractImages)
        - [ExtractImagesFile(inFile, outDir, selectedPages, conf)](#ExtractImagesFile)
        - [ExtractImagesRaw(rs, selectedPages, conf)](#ExtractImagesRaw)
        - [ExtractMetadata(rs, outDir, fileName, conf)](#ExtractMetadata)
        - [ExtractMetadataFile(inFile, outDir, conf)](#ExtractMetadataFile)
        - [ExtractPage(ctx, pageNr)](#ExtractPage)
        - [ExtractPages(rs, outDir, fileName, selectedPages, conf)](#ExtractPages)
        - [ExtractPagesFile(inFile, outDir, selectedPages, conf)](#ExtractPagesFile)
        - [FillForm(rs, rd, w, conf)](#FillForm)
        - [FillFormFile(inFilePDF, inFileJSON, outFilePDF, conf)](#FillFormFile)
        - [FormFields(rs, conf)](#FormFields)
        - [GetPermissions(rs, conf)](#GetPermissions)
        - [GetPermissionsFile(inFile, conf)](#GetPermissionsFile)
        - [HasWatermarks(rs, conf)](#HasWatermarks)
        - [HasWatermarksFile(inFile, conf)](#HasWatermarksFile)
        - [ImageBookletConfig(val, desc, conf)](#ImageBookletConfig)
        - [ImageGridConfig(rows, cols, desc, conf)](#ImageGridConfig)
        - [ImageNUpConfig(val, desc, conf)](#ImageNUpConfig)
        - [ImageWatermark(fileName, desc, onTop, update, u)](#ImageWatermark)
        - [ImageWatermarkForReader(r, desc, onTop, update, u)](#ImageWatermarkForReader)
        - [Images(rs, selectedPages, conf)](#Images)
        - [Import(s, u)](#Import)
        - [ImportBookmarks(rs, rd, w, replace, conf)](#ImportBookmarks)
        - [ImportBookmarksFile(inFilePDF, inFileJSON, outFilePDF, replace, conf)](#ImportBookmarksFile)
        - [ImportCertificates(inFiles)](#ImportCertificates)
        - [ImportImages(rs, w, imgs, imp, conf)](#ImportImages)
        - [ImportImagesFile(imgFiles, outFile, imp, conf)](#ImportImagesFile)
        - [InsertPages(rs, w, selectedPages, before, pageConf, conf)](#InsertPages)
        - [InsertPagesFile(inFile, outFile, selectedPages, before, pageConf, conf)](#InsertPagesFile)
        - [InspectCertificates(inFiles)](#InspectCertificates)
        - [InstallFonts(fileNames)](#InstallFonts)
        - [Keywords(rs, conf)](#Keywords)
        - [ListFonts()](#ListFonts)
        - [ListPageLayout(rs, conf)](#ListPageLayout)
        - [ListPageLayoutFile(inFile, conf)](#ListPageLayoutFile)
        - [ListPageMode(rs, conf)](#ListPageMode)
        - [ListPageModeFile(inFile, conf)](#ListPageModeFile)
        - [ListViewerPreferences(rs, all, conf)](#ListViewerPreferences)
        - [ListViewerPreferencesFile(inFile, all, json, conf)](#ListViewerPreferencesFile)
        - [ListViewerPreferencesFileJSON(inFile, all, conf)](#ListViewerPreferencesFileJSON)
        - [LoadCertificates()](#LoadCertificates)
        - [LoadConfiguration()](#LoadConfiguration)
        - [LockFormFields(rs, w, fieldIDsOrNames, conf)](#LockFormFields)
        - [LockFormFieldsFile(inFile, outFile, fieldIDsOrNames, conf)](#LockFormFieldsFile)
        - [Merge(destFile, inFiles, w, conf, dividerPage)](#Merge)
        - [MergeAppendFile(inFiles, outFile, dividerPage, conf)](#MergeAppendFile)
        - [MergeCreateFile(inFiles, outFile, dividerPage, conf)](#MergeCreateFile)
        - [MergeCreateZip(rs1, rs2, w, conf)](#MergeCreateZip)
        - [MergeCreateZipFile(inFile1, inFile2, outFile, conf)](#MergeCreateZipFile)
        - [MergeRaw(rsc, w, dividerPage, conf)](#MergeRaw)
        - [MultiFillForm(inFilePDF, rd, outDir, fileName, format, merge, conf)](#MultiFillForm)
        - [MultiFillFormFile(inFilePDF, inFileData, outDir, outFilePDF, merge, conf)](#MultiFillFormFile)
        - [NDown(rs, outDir, fileName, selectedPages, n, cut, conf)](#NDown)
        - [NDownFile(inFile, outDir, outFile, selectedPages, n, cut, conf)](#NDownFile)
        - [NUp(rs, w, imgFiles, selectedPages, nup, conf)](#NUp)
        - [NUpFile(inFiles, outFile, selectedPages, nup, conf)](#NUpFile)
        - [NUpFromImage(conf, imageFileNames, nup)](#NUpFromImage)
        - [Optimize(rs, w, conf)](#Optimize)
        - [OptimizeContext(ctx)](#OptimizeContext)
        - [OptimizeFile(inFile, outFile, conf)](#OptimizeFile)
        - [PDFBookletConfig(val, desc, conf)](#PDFBookletConfig)
        - [PDFGridConfig(rows, cols, desc, conf)](#PDFGridConfig)
        - [PDFInfo(rs, fileName, selectedPages, fonts, conf)](#PDFInfo)
        - [PDFMultiWatermarkForReadSeeker(rs, startPageNrSrc, startPageNrDest, desc, onTop, update, u)](#PDFMultiWatermarkForReadSeeker)
        - [PDFNUpConfig(val, desc, conf)](#PDFNUpConfig)
        - [PDFWatermark(fileName, desc, onTop, update, u)](#PDFWatermark)
        - [PDFWatermarkForReadSeeker(rs, pageNrSrc, desc, onTop, update, u)](#PDFWatermarkForReadSeeker)
        - [PageBoundaries(s, unit)](#PageBoundaries)
        - [PageBoundariesFromBoxList(s)](#PageBoundariesFromBoxList)
        - [PageCount(rs, conf)](#PageCount)
        - [PageCountFile(inFile)](#PageCountFile)
        - [PageDims(rs, conf)](#PageDims)
        - [PageDimsFile(inFile)](#PageDimsFile)
        - [PageLayout(rs, conf)](#PageLayout)
        - [PageLayoutFile(inFile, conf)](#PageLayoutFile)
        - [PageMode(rs, conf)](#PageMode)
        - [PageModeFile(inFile, conf)](#PageModeFile)
        - [PagesForPageCollection(pageCount, pageSelection)](#PagesForPageCollection)
        - [PagesForPageRange(from, thru)](#PagesForPageRange)
        - [PagesForPageSelection(pageCount, pageSelection, ensureAllforNone, log)](#PagesForPageSelection)
        - [ParsePageSelection(s)](#ParsePageSelection)
        - [Permissions(rs, conf)](#Permissions)
        - [Poster(rs, outDir, fileName, selectedPages, cut, conf)](#Poster)
        - [PosterFile(inFile, outDir, outFile, selectedPages, cut, conf)](#PosterFile)
        - [Properties(rs, conf)](#Properties)
        - [ReadAndValidate(rs, conf)](#ReadAndValidate)
        - [ReadContext(rs, conf)](#ReadContext)
        - [ReadContextFile(inFile)](#ReadContextFile)
        - [ReadValidateAndOptimize(rs, conf)](#ReadValidateAndOptimize)
        - [RemainingPagesForPageRemoval(pageCount, pageSelection, log)](#RemainingPagesForPageRemoval)
        - [RemoveAnnotations(rs, w, selectedPages, idsAndTypes, objNrs, conf)](#RemoveAnnotations)
        - [RemoveAnnotationsAsIncrement(rws, selectedPages, idsAndTypes, objNrs, conf)](#RemoveAnnotationsAsIncrement)
        - [RemoveAnnotationsFile(inFile, outFile, selectedPages, idsAndTypes, objNrs, conf, incr)](#RemoveAnnotationsFile)
        - [RemoveAttachments(rs, w, files, conf)](#RemoveAttachments)
        - [RemoveAttachmentsFile(inFile, outFile, files, conf)](#RemoveAttachmentsFile)
        - [RemoveBookmarks(rs, w, conf)](#RemoveBookmarks)
        - [RemoveBookmarksFile(inFile, outFile, conf)](#RemoveBookmarksFile)
        - [RemoveBoxes(rs, w, selectedPages, pb, conf)](#RemoveBoxes)
        - [RemoveBoxesFile(inFile, outFile, selectedPages, pb, conf)](#RemoveBoxesFile)
        - [RemoveFormFields(rs, w, fieldIDsOrNames, conf)](#RemoveFormFields)
        - [RemoveFormFieldsFile(inFile, outFile, fieldIDsOrNames, conf)](#RemoveFormFieldsFile)
        - [RemoveKeywords(rs, w, keywords, conf)](#RemoveKeywords)
        - [RemoveKeywordsFile(inFile, outFile, keywords, conf)](#RemoveKeywordsFile)
        - [RemovePages(rs, w, selectedPages, conf)](#RemovePages)
        - [RemovePagesFile(inFile, outFile, selectedPages, conf)](#RemovePagesFile)
        - [RemoveProperties(rs, w, properties, conf)](#RemoveProperties)
        - [RemovePropertiesFile(inFile, outFile, properties, conf)](#RemovePropertiesFile)
        - [RemoveWatermarks(rs, w, selectedPages, conf)](#RemoveWatermarks)
        - [RemoveWatermarksFile(inFile, outFile, selectedPages, conf)](#RemoveWatermarksFile)
        - [ResetFormFields(rs, w, fieldIDsOrNames, conf)](#ResetFormFields)
        - [ResetFormFieldsFile(inFile, outFile, fieldIDsOrNames, conf)](#ResetFormFieldsFile)
        - [ResetPageLayout(rs, w, conf)](#ResetPageLayout)
        - [ResetPageLayoutFile(inFile, outFile, conf)](#ResetPageLayoutFile)
        - [ResetPageMode(rs, w, conf)](#ResetPageMode)
        - [ResetPageModeFile(inFile, outFile, conf)](#ResetPageModeFile)
        - [ResetViewerPreferences(rs, w, conf)](#ResetViewerPreferences)
        - [ResetViewerPreferencesFile(inFile, outFile, conf)](#ResetViewerPreferencesFile)
        - [Resize(rs, w, selectedPages, resize, conf)](#Resize)
        - [ResizeFile(inFile, outFile, selectedPages, resize, conf)](#ResizeFile)
        - [Rotate(rs, w, rotation, selectedPages, conf)](#Rotate)
        - [RotateFile(inFile, outFile, rotation, selectedPages, conf)](#RotateFile)
        - [SetPageLayout(rs, w, val, conf)](#SetPageLayout)
        - [SetPageLayoutFile(inFile, outFile, val, conf)](#SetPageLayoutFile)
        - [SetPageMode(rs, w, val, conf)](#SetPageMode)
        - [SetPageModeFile(inFile, outFile, val, conf)](#SetPageModeFile)
        - [SetPermissions(rs, w, conf)](#SetPermissions)
        - [SetPermissionsFile(inFile, outFile, conf)](#SetPermissionsFile)
        - [SetViewerPreferences(rs, w, vp, conf)](#SetViewerPreferences)
        - [SetViewerPreferencesFile(inFile, outFile, vp, conf)](#SetViewerPreferencesFile)
        - [SetViewerPreferencesFileFromJSONBytes(inFile, outFile, jsonBytes, conf)](#SetViewerPreferencesFileFromJSONBytes)
        - [SetViewerPreferencesFileFromJSONFile(inFilePDF, outFilePDF, inFileJSON, conf)](#SetViewerPreferencesFileFromJSONFile)
        - [SetViewerPreferencesFromJSONBytes(rs, w, jsonBytes, conf)](#SetViewerPreferencesFromJSONBytes)
        - [SetViewerPreferencesFromJSONReader(rs, w, rd, conf)](#SetViewerPreferencesFromJSONReader)
        - [Split(rs, outDir, fileName, span, conf)](#Split)
        - [SplitByPageNr(rs, outDir, fileName, pageNrs, conf)](#SplitByPageNr)
        - [SplitByPageNrFile(inFile, outDir, pageNrs, conf)](#SplitByPageNrFile)
        - [SplitFile(inFile, outDir, span, conf)](#SplitFile)
        - [TextWatermark(text, desc, onTop, update, u)](#TextWatermark)
        - [Trim(rs, w, selectedPages, conf)](#Trim)
        - [TrimFile(inFile, outFile, selectedPages, conf)](#TrimFile)
        - [UnlockFormFields(rs, w, fieldIDsOrNames, conf)](#UnlockFormFields)
        - [UnlockFormFieldsFile(inFile, outFile, fieldIDsOrNames, conf)](#UnlockFormFieldsFile)
        - [UpdateImageWatermarksFile(inFile, outFile, selectedPages, onTop, fileName, desc, conf)](#UpdateImageWatermarksFile)
        - [UpdateImages(rs, rd, w, objNr, pageNr, id, conf)](#UpdateImages)
        - [UpdateImagesFile(inFile, imageFile, outFile, objNr, pageNr, id, conf)](#UpdateImagesFile)
        - [UpdatePDFWatermarksFile(inFile, outFile, selectedPages, onTop, fileName, desc, conf)](#UpdatePDFWatermarksFile)
        - [UpdateTextWatermarksFile(inFile, outFile, selectedPages, onTop, text, desc, conf)](#UpdateTextWatermarksFile)
        - [Validate(rs, conf)](#Validate)
        - [ValidateContext(ctx)](#ValidateContext)
        - [ValidateFile(inFile, conf)](#ValidateFile)
        - [ValidateFiles(inFiles, conf)](#ValidateFiles)
        - [ValidateSignatures(inFile, all, conf)](#ValidateSignatures)
        - [ValidateSignaturesFile(inFile, all, full, conf)](#ValidateSignaturesFile)
        - [ViewerPreferences(rs, conf)](#ViewerPreferences)
        - [ViewerPreferencesFile(inFile, all, conf)](#ViewerPreferencesFile)
        - [WatermarkContext(ctx, selectedPages, wm)](#WatermarkContext)
        - [Write(ctx, w, conf)](#Write)
        - [WriteContext(ctx, w)](#WriteContext)
        - [WriteContextFile(ctx, outFile)](#WriteContextFile)
        - [WriteIncr(ctx, rws, conf)](#WriteIncr)
        - [WriteIncrement(ctx, w)](#WriteIncrement)
        - [WritePage(r, outDir, fileName, pageNr)](#WritePage)
        - [Zoom(rs, w, selectedPages, zoom, conf)](#Zoom)
        - [ZoomFile(inFile, outFile, selectedPages, zoom, conf)](#ZoomFile)
    - [Types](#pkg-types)
        - [type PageSpan](#PageSpan)
            - [SplitRaw(rs, span, conf)](#SplitRaw)
- [Source Files](#section-sourcefiles)

Documentation

## [Documentation ¶](#section-documentation)

<!-- image -->

### [Overview ¶](#pkg-overview)

Package api lets you integrate pdfcpu's operations into your Go backend.

There are two api layers supporting all pdfcpu operations:

1. The file based layer (used by pdfcpu's cli)
2. The io.ReadSeeker/io.Writer based layer for backend integration.

For any pdfcpu command there are two functions.

The file based function always calls the io.ReadSeeker/io.Writer based function:

```
func CommandFile(inFile, outFile string, conf *pdf.Configuration) error
func Command(rs io.ReadSeeker, w io.Writer, conf *pdf.Configuration) error
```

eg. for optimization:

```
func OptimizeFile(inFile, outFile string, conf *pdf.Configuration) error
func Optimize(rs io.ReadSeeker, w io.Writer, conf *pdf.Configuration) error
```

### [Index ¶](#pkg-index)

- [Variables](#pkg-variables)
- [func AddAnnotations(rs io.ReadSeeker, w io.Writer, selectedPages []string, ...) error](#AddAnnotations)
- [func AddAnnotationsAsIncrement(rws io.ReadWriteSeeker, selectedPages []string, ar model.AnnotationRenderer, ...) error](#AddAnnotationsAsIncrement)
- [func AddAnnotationsFile(inFile, outFile string, selectedPages []string, ar model.AnnotationRenderer, ...) (err error)](#AddAnnotationsFile)
- [func AddAnnotationsMap(rs io.ReadSeeker, w io.Writer, m map[int][]model.AnnotationRenderer, ...) error](#AddAnnotationsMap)
- [func AddAnnotationsMapAsIncrement(rws io.ReadWriteSeeker, m map[int][]model.AnnotationRenderer, ...) error](#AddAnnotationsMapAsIncrement)
- [func AddAnnotationsMapFile(inFile, outFile string, m map[int][]model.AnnotationRenderer, ...) (err error)](#AddAnnotationsMapFile)
- [func AddAttachments(rs io.ReadSeeker, w io.Writer, files []string, coll bool, ...) error](#AddAttachments)
- [func AddAttachmentsFile(inFile, outFile string, files []string, coll bool, conf *model.Configuration) (err error)](#AddAttachmentsFile)
- [func AddBookmarks(rs io.ReadSeeker, w io.Writer, bms []pdfcpu.Bookmark, replace bool, ...) error](#AddBookmarks)
- [func AddBookmarksFile(inFile, outFile string, bms []pdfcpu.Bookmark, replace bool, ...) (err error)](#AddBookmarksFile)
- [func AddBoxes(rs io.ReadSeeker, w io.Writer, selectedPages []string, ...) error](#AddBoxes)
- [func AddBoxesFile(inFile, outFile string, selectedPages []string, pb *model.PageBoundaries, ...) (err error)](#AddBoxesFile)
- [func AddImageWatermarksFile(inFile, outFile string, selectedPages []string, onTop bool, ...) error](#AddImageWatermarksFile)
- [func AddImageWatermarksForReaderFile(inFile, outFile string, selectedPages []string, onTop bool, r io.Reader, ...) error](#AddImageWatermarksForReaderFile)
- [func AddKeywords(rs io.ReadSeeker, w io.Writer, files []string, conf *model.Configuration) error](#AddKeywords)
- [func AddKeywordsFile(inFile, outFile string, files []string, conf *model.Configuration) (err error)](#AddKeywordsFile)
- [func AddPDFWatermarksFile(inFile, outFile string, selectedPages []string, onTop bool, ...) error](#AddPDFWatermarksFile)
- [func AddProperties(rs io.ReadSeeker, w io.Writer, properties map[string]string, ...) error](#AddProperties)
- [func AddPropertiesFile(inFile, outFile string, properties map[string]string, ...) (err error)](#AddPropertiesFile)
- [func AddTextWatermarksFile(inFile, outFile string, selectedPages []string, onTop bool, text, desc string, ...) error](#AddTextWatermarksFile)
- [func AddWatermarks(rs io.ReadSeeker, w io.Writer, selectedPages []string, wm *model.Watermark, ...) error](#AddWatermarks)
- [func AddWatermarksFile(inFile, outFile string, selectedPages []string, wm *model.Watermark, ...) (err error)](#AddWatermarksFile)
- [func AddWatermarksMap(rs io.ReadSeeker, w io.Writer, m map[int]*model.Watermark, ...) error](#AddWatermarksMap)
- [func AddWatermarksMapFile(inFile, outFile string, m map[int]*model.Watermark, conf *model.Configuration) (err error)](#AddWatermarksMapFile)
- [func AddWatermarksSliceMap(rs io.ReadSeeker, w io.Writer, m map[int][]*model.Watermark, ...) error](#AddWatermarksSliceMap)
- [func AddWatermarksSliceMapFile(inFile, outFile string, m map[int][]*model.Watermark, ...) (err error)](#AddWatermarksSliceMapFile)
- [func Annotations(rs io.ReadSeeker, selectedPages []string, conf *model.Configuration) (map[int]model.PgAnnots, error)](#Annotations)
- [func Attachments(rs io.ReadSeeker, conf *model.Configuration) ([]model.Attachment, error)](#Attachments)
- [func Booklet(rs io.ReadSeeker, w io.Writer, imgFiles, selectedPages []string, ...) error](#Booklet)
- [func BookletFile(inFiles []string, outFile string, selectedPages []string, nup *model.NUp, ...) (err error)](#BookletFile)
- [func BookletFromImages(conf *model.Configuration, imageFileNames []string, nup *model.NUp) (*model.Context, error)](#BookletFromImages)
- [func Bookmarks(rs io.ReadSeeker, conf *model.Configuration) ([]pdfcpu.Bookmark, error)](#Bookmarks)
- [func Box(s string, u types.DisplayUnit) (*model.Box, error)](#Box)
- [func Boxes(rs io.ReadSeeker, selectedPages []string, conf *model.Configuration) ([]model.PageBoundaries, error)](#Boxes)
- [func ChangeOwnerPassword(rs io.ReadSeeker, w io.Writer, pwOld, pwNew string, conf *model.Configuration) error](#ChangeOwnerPassword)
- [func ChangeOwnerPasswordFile(inFile, outFile string, pwOld, pwNew string, conf *model.Configuration) (err error)](#ChangeOwnerPasswordFile)
- [func ChangeUserPassword(rs io.ReadSeeker, w io.Writer, pwOld, pwNew string, conf *model.Configuration) error](#ChangeUserPassword)
- [func ChangeUserPasswordFile(inFile, outFile string, pwOld, pwNew string, conf *model.Configuration) (err error)](#ChangeUserPasswordFile)
- [func Collect(rs io.ReadSeeker, w io.Writer, selectedPages []string, ...) error](#Collect)
- [func CollectFile(inFile, outFile string, selectedPages []string, conf *model.Configuration) (err error)](#CollectFile)
- [func Create(rs io.ReadSeeker, rd io.Reader, w io.Writer, conf *model.Configuration) error](#Create)
- [func CreateCheatSheetsUserFonts(fontNames []string) error](#CreateCheatSheetsUserFonts)
- [func CreateFile(inFilePDF, inFileJSON, outFilePDF string, conf *model.Configuration) (err error)](#CreateFile)
- [func CreatePDFFile(xRefTable *model.XRefTable, outFile string, conf *model.Configuration) error](#CreatePDFFile)
- [func CreateUserFontDemoFiles(dir, fn string) error](#CreateUserFontDemoFiles)
- [func Crop(rs io.ReadSeeker, w io.Writer, selectedPages []string, b *model.Box, ...) error](#Crop)
- [func CropFile(inFile, outFile string, selectedPages []string, b *model.Box, ...) (err error)](#CropFile)
- [func Cut(rs io.ReadSeeker, outDir, fileName string, selectedPages []string, ...) error](#Cut)
- [func CutFile(inFile, outDir, outFile string, selectedPages []string, cut *model.Cut, ...) error](#CutFile)
- [func Decrypt(rs io.ReadSeeker, w io.Writer, conf *model.Configuration) error](#Decrypt)
- [func DecryptFile(inFile, outFile string, conf *model.Configuration) (err error)](#DecryptFile)
- [func DisableConfigDir()](#DisableConfigDir)
- [func DumpObject(rs io.ReadSeeker, mode, objNr int, conf *model.Configuration) error](#DumpObject)
- [func DumpObjectFile(inFile string, mode, objNr int, conf *model.Configuration) error](#DumpObjectFile)
- [func Encrypt(rs io.ReadSeeker, w io.Writer, conf *model.Configuration) error](#Encrypt)
- [func EncryptFile(inFile, outFile string, conf *model.Configuration) (err error)](#EncryptFile)
- [func EnsureDefaultConfigAt(path string) error](#EnsureDefaultConfigAt)
- [func ExportBookmarksFile(inFilePDF, outFileJSON string, conf *model.Configuration) (err error)](#ExportBookmarksFile)
- [func ExportBookmarksJSON(rs io.ReadSeeker, w io.Writer, source string, conf *model.Configuration) error](#ExportBookmarksJSON)
- [func ExportForm(rs io.ReadSeeker, source string, conf *model.Configuration) (*form.FormGroup, error)](#ExportForm)
- [func ExportFormFile(inFilePDF, outFileJSON string, conf *model.Configuration) (err error)](#ExportFormFile)
- [func ExportFormJSON(rs io.ReadSeeker, w io.Writer, source string, conf *model.Configuration) error](#ExportFormJSON)
- [func ExtractAttachments(rs io.ReadSeeker, outDir string, fileNames []string, conf *model.Configuration) error](#ExtractAttachments)
- [func ExtractAttachmentsFile(inFile, outDir string, files []string, conf *model.Configuration) error](#ExtractAttachmentsFile)
- [func ExtractAttachmentsRaw(rs io.ReadSeeker, outDir string, fileNames []string, conf *model.Configuration) ([]model.Attachment, error)](#ExtractAttachmentsRaw)
- [func ExtractContent(rs io.ReadSeeker, outDir, fileName string, selectedPages []string, ...) error](#ExtractContent)
- [func ExtractContentFile(inFile, outDir string, selectedPages []string, conf *model.Configuration) error](#ExtractContentFile)
- [func ExtractFonts(rs io.ReadSeeker, outDir, fileName string, selectedPages []string, ...) error](#ExtractFonts)
- [func ExtractFontsFile(inFile, outDir string, selectedPages []string, conf *model.Configuration) error](#ExtractFontsFile)
- [func ExtractImages(rs io.ReadSeeker, selectedPages []string, ...) error](#ExtractImages)
- [func ExtractImagesFile(inFile, outDir string, selectedPages []string, conf *model.Configuration) error](#ExtractImagesFile)
- [func ExtractImagesRaw(rs io.ReadSeeker, selectedPages []string, conf *model.Configuration) ([]map[int]model.Image, error)](#ExtractImagesRaw)
- [func ExtractMetadata(rs io.ReadSeeker, outDir, fileName string, conf *model.Configuration) error](#ExtractMetadata)
- [func ExtractMetadataFile(inFile, outDir string, conf *model.Configuration) error](#ExtractMetadataFile)
- [func ExtractPage(ctx *model.Context, pageNr int) (io.Reader, error)](#ExtractPage)
- [func ExtractPages(rs io.ReadSeeker, outDir, fileName string, selectedPages []string, ...) error](#ExtractPages)
- [func ExtractPagesFile(inFile, outDir string, selectedPages []string, conf *model.Configuration) error](#ExtractPagesFile)
- [func FillForm(rs io.ReadSeeker, rd io.Reader, w io.Writer, conf *model.Configuration) error](#FillForm)
- [func FillFormFile(inFilePDF, inFileJSON, outFilePDF string, conf *model.Configuration) (err error)](#FillFormFile)
- [func FormFields(rs io.ReadSeeker, conf *model.Configuration) ([]form.Field, error)](#FormFields)
- [func GetPermissions(rs io.ReadSeeker, conf *model.Configuration) (*int16, error)](#GetPermissions)
- [func GetPermissionsFile(inFile string, conf *model.Configuration) (*int16, error)](#GetPermissionsFile)
- [func HasWatermarks(rs io.ReadSeeker, conf *model.Configuration) (bool, error)](#HasWatermarks)
- [func HasWatermarksFile(inFile string, conf *model.Configuration) (bool, error)](#HasWatermarksFile)
- [func ImageBookletConfig(val int, desc string, conf *model.Configuration) (*model.NUp, error)](#ImageBookletConfig)
- [func ImageGridConfig(rows, cols int, desc string, conf *model.Configuration) (*model.NUp, error)](#ImageGridConfig)
- [func ImageNUpConfig(val int, desc string, conf *model.Configuration) (*model.NUp, error)](#ImageNUpConfig)
- [func ImageWatermark(fileName, desc string, onTop, update bool, u types.DisplayUnit) (*model.Watermark, error)](#ImageWatermark)
- [func ImageWatermarkForReader(r io.Reader, desc string, onTop, update bool, u types.DisplayUnit) (*model.Watermark, error)](#ImageWatermarkForReader)
- [func Images(rs io.ReadSeeker, selectedPages []string, conf *model.Configuration) ([]map[int]model.Image, error)](#Images)
- [func Import(s string, u types.DisplayUnit) (*pdfcpu.Import, error)](#Import)
- [func ImportBookmarks(rs io.ReadSeeker, rd io.Reader, w io.Writer, replace bool, ...) error](#ImportBookmarks)
- [func ImportBookmarksFile(inFilePDF, inFileJSON, outFilePDF string, replace bool, ...) (err error)](#ImportBookmarksFile)
- [func ImportCertificates(inFiles []string) ([]string, error)](#ImportCertificates)
- [func ImportImages(rs io.ReadSeeker, w io.Writer, imgs []io.Reader, imp *pdfcpu.Import, ...) error](#ImportImages)
- [func ImportImagesFile(imgFiles []string, outFile string, imp *pdfcpu.Import, ...) (err error)](#ImportImagesFile)
- [func InsertPages(rs io.ReadSeeker, w io.Writer, selectedPages []string, before bool, ...) error](#InsertPages)
- [func InsertPagesFile(inFile, outFile string, selectedPages []string, before bool, ...) (err error)](#InsertPagesFile)
- [func InspectCertificates(inFiles []string) ([]string, error)](#InspectCertificates)
- [func InstallFonts(fileNames []string) error](#InstallFonts)
- [func Keywords(rs io.ReadSeeker, conf *model.Configuration) ([]string, error)](#Keywords)
- [func ListFonts() ([]string, error)](#ListFonts)
- [func ListPageLayout(rs io.ReadSeeker, conf *model.Configuration) ([]string, error)](#ListPageLayout)
- [func ListPageLayoutFile(inFile string, conf *model.Configuration) ([]string, error)](#ListPageLayoutFile)
- [func ListPageMode(rs io.ReadSeeker, conf *model.Configuration) ([]string, error)](#ListPageMode)
- [func ListPageModeFile(inFile string, conf *model.Configuration) ([]string, error)](#ListPageModeFile)
- [func ListViewerPreferences(rs io.ReadSeeker, all bool, conf *model.Configuration) ([]string, error)](#ListViewerPreferences)
- [func ListViewerPreferencesFile(inFile string, all, json bool, conf *model.Configuration) ([]string, error)](#ListViewerPreferencesFile)
- [func ListViewerPreferencesFileJSON(inFile string, all bool, conf *model.Configuration) ([]string, error)](#ListViewerPreferencesFileJSON)
- [func LoadCertificates() (int, error)](#LoadCertificates)
- [func LoadConfiguration() *model.Configuration](#LoadConfiguration)
- [func LockFormFields(rs io.ReadSeeker, w io.Writer, fieldIDsOrNames []string, ...) error](#LockFormFields)
- [func LockFormFieldsFile(inFile, outFile string, fieldIDsOrNames []string, conf *model.Configuration) (err error)](#LockFormFieldsFile)
- [func Merge(destFile string, inFiles []string, w io.Writer, conf *model.Configuration, ...) error](#Merge)
- [func MergeAppendFile(inFiles []string, outFile string, dividerPage bool, conf *model.Configuration) (err error)](#MergeAppendFile)
- [func MergeCreateFile(inFiles []string, outFile string, dividerPage bool, conf *model.Configuration) (err error)](#MergeCreateFile)
- [func MergeCreateZip(rs1, rs2 io.ReadSeeker, w io.Writer, conf *model.Configuration) error](#MergeCreateZip)
- [func MergeCreateZipFile(inFile1, inFile2, outFile string, conf *model.Configuration) (err error)](#MergeCreateZipFile)
- [func MergeRaw(rsc []io.ReadSeeker, w io.Writer, dividerPage bool, conf *model.Configuration) error](#MergeRaw)
- [func MultiFillForm(inFilePDF string, rd io.Reader, outDir, fileName string, ...) error](#MultiFillForm)
- [func MultiFillFormFile(inFilePDF, inFileData, outDir, outFilePDF string, merge bool, ...) (err error)](#MultiFillFormFile)
- [func NDown(rs io.ReadSeeker, outDir, fileName string, selectedPages []string, n int, ...) error](#NDown)
- [func NDownFile(inFile, outDir, outFile string, selectedPages []string, n int, cut *model.Cut, ...) error](#NDownFile)
- [func NUp(rs io.ReadSeeker, w io.Writer, imgFiles, selectedPages []string, ...) error](#NUp)
- [func NUpFile(inFiles []string, outFile string, selectedPages []string, nup *model.NUp, ...) (err error)](#NUpFile)
- [func NUpFromImage(conf *model.Configuration, imageFileNames []string, nup *model.NUp) (*model.Context, error)](#NUpFromImage)
- [func Optimize(rs io.ReadSeeker, w io.Writer, conf *model.Configuration) error](#Optimize)
- [func OptimizeContext(ctx *model.Context) error](#OptimizeContext)
- [func OptimizeFile(inFile, outFile string, conf *model.Configuration) (err error)](#OptimizeFile)
- [func PDFBookletConfig(val int, desc string, conf *model.Configuration) (*model.NUp, error)](#PDFBookletConfig)
- [func PDFGridConfig(rows, cols int, desc string, conf *model.Configuration) (*model.NUp, error)](#PDFGridConfig)
- [func PDFInfo(rs io.ReadSeeker, fileName string, selectedPages []string, fonts bool, ...) (*pdfcpu.PDFInfo, error)](#PDFInfo)
- [func PDFMultiWatermarkForReadSeeker(rs io.ReadSeeker, startPageNrSrc, startPageNrDest int, desc string, ...) (*model.Watermark, error)](#PDFMultiWatermarkForReadSeeker)
- [func PDFNUpConfig(val int, desc string, conf *model.Configuration) (*model.NUp, error)](#PDFNUpConfig)
- [func PDFWatermark(fileName, desc string, onTop, update bool, u types.DisplayUnit) (*model.Watermark, error)](#PDFWatermark)
- [func PDFWatermarkForReadSeeker(rs io.ReadSeeker, pageNrSrc int, desc string, onTop, update bool, ...) (*model.Watermark, error)](#PDFWatermarkForReadSeeker)
- [func PageBoundaries(s string, unit types.DisplayUnit) (*model.PageBoundaries, error)](#PageBoundaries)
- [func PageBoundariesFromBoxList(s string) (*model.PageBoundaries, error)](#PageBoundariesFromBoxList)
- [func PageCount(rs io.ReadSeeker, conf *model.Configuration) (int, error)](#PageCount)
- [func PageCountFile(inFile string) (int, error)](#PageCountFile)
- [func PageDims(rs io.ReadSeeker, conf *model.Configuration) ([]types.Dim, error)](#PageDims)
- [func PageDimsFile(inFile string) ([]types.Dim, error)](#PageDimsFile)
- [func PageLayout(rs io.ReadSeeker, conf *model.Configuration) (*model.PageLayout, error)](#PageLayout)
- [func PageLayoutFile(inFile string, conf *model.Configuration) (*model.PageLayout, error)](#PageLayoutFile)
- [func PageMode(rs io.ReadSeeker, conf *model.Configuration) (*model.PageMode, error)](#PageMode)
- [func PageModeFile(inFile string, conf *model.Configuration) (*model.PageMode, error)](#PageModeFile)
- [func PagesForPageCollection(pageCount int, pageSelection []string) ([]int, error)](#PagesForPageCollection)
- [func PagesForPageRange(from, thru int) []int](#PagesForPageRange)
- [func PagesForPageSelection(pageCount int, pageSelection []string, ensureAllforNone bool, log bool) (types.IntSet, error)](#PagesForPageSelection)
- [func ParsePageSelection(s string) ([]string, error)](#ParsePageSelection)
- [func Permissions(rs io.ReadSeeker, conf *model.Configuration) (int, error)](#Permissions)
- [func Poster(rs io.ReadSeeker, outDir, fileName string, selectedPages []string, ...) error](#Poster)
- [func PosterFile(inFile, outDir, outFile string, selectedPages []string, cut *model.Cut, ...) error](#PosterFile)
- [func Properties(rs io.ReadSeeker, conf *model.Configuration) (map[string]string, error)](#Properties)
- [func ReadAndValidate(rs io.ReadSeeker, conf *model.Configuration) (ctx *model.Context, err error)](#ReadAndValidate)
- [func ReadContext(rs io.ReadSeeker, conf *model.Configuration) (*model.Context, error)](#ReadContext)
- [func ReadContextFile(inFile string) (*model.Context, error)](#ReadContextFile)
- [func ReadValidateAndOptimize(rs io.ReadSeeker, conf *model.Configuration) (ctx *model.Context, err error)](#ReadValidateAndOptimize)
- [func RemainingPagesForPageRemoval(pageCount int, pageSelection []string, log bool) (types.IntSet, error)](#RemainingPagesForPageRemoval)
- [func RemoveAnnotations(rs io.ReadSeeker, w io.Writer, selectedPages, idsAndTypes []string, ...) error](#RemoveAnnotations)
- [func RemoveAnnotationsAsIncrement(rws io.ReadWriteSeeker, selectedPages, idsAndTypes []string, objNrs []int, ...) error](#RemoveAnnotationsAsIncrement)
- [func RemoveAnnotationsFile(inFile, outFile string, selectedPages, idsAndTypes []string, objNrs []int, ...) (err error)](#RemoveAnnotationsFile)
- [func RemoveAttachments(rs io.ReadSeeker, w io.Writer, files []string, conf *model.Configuration) error](#RemoveAttachments)
- [func RemoveAttachmentsFile(inFile, outFile string, files []string, conf *model.Configuration) (err error)](#RemoveAttachmentsFile)
- [func RemoveBookmarks(rs io.ReadSeeker, w io.Writer, conf *model.Configuration) error](#RemoveBookmarks)
- [func RemoveBookmarksFile(inFile, outFile string, conf *model.Configuration) (err error)](#RemoveBookmarksFile)
- [func RemoveBoxes(rs io.ReadSeeker, w io.Writer, selectedPages []string, ...) error](#RemoveBoxes)
- [func RemoveBoxesFile(inFile, outFile string, selectedPages []string, pb *model.PageBoundaries, ...) (err error)](#RemoveBoxesFile)
- [func RemoveFormFields(rs io.ReadSeeker, w io.Writer, fieldIDsOrNames []string, ...) error](#RemoveFormFields)
- [func RemoveFormFieldsFile(inFile, outFile string, fieldIDsOrNames []string, conf *model.Configuration) (err error)](#RemoveFormFieldsFile)
- [func RemoveKeywords(rs io.ReadSeeker, w io.Writer, keywords []string, conf *model.Configuration) error](#RemoveKeywords)
- [func RemoveKeywordsFile(inFile, outFile string, keywords []string, conf *model.Configuration) (err error)](#RemoveKeywordsFile)
- [func RemovePages(rs io.ReadSeeker, w io.Writer, selectedPages []string, ...) error](#RemovePages)
- [func RemovePagesFile(inFile, outFile string, selectedPages []string, conf *model.Configuration) (err error)](#RemovePagesFile)
- [func RemoveProperties(rs io.ReadSeeker, w io.Writer, properties []string, conf *model.Configuration) error](#RemoveProperties)
- [func RemovePropertiesFile(inFile, outFile string, properties []string, conf *model.Configuration) (err error)](#RemovePropertiesFile)
- [func RemoveWatermarks(rs io.ReadSeeker, w io.Writer, selectedPages []string, ...) error](#RemoveWatermarks)
- [func RemoveWatermarksFile(inFile, outFile string, selectedPages []string, conf *model.Configuration) (err error)](#RemoveWatermarksFile)
- [func ResetFormFields(rs io.ReadSeeker, w io.Writer, fieldIDsOrNames []string, ...) error](#ResetFormFields)
- [func ResetFormFieldsFile(inFile, outFile string, fieldIDsOrNames []string, conf *model.Configuration) (err error)](#ResetFormFieldsFile)
- [func ResetPageLayout(rs io.ReadSeeker, w io.Writer, conf *model.Configuration) error](#ResetPageLayout)
- [func ResetPageLayoutFile(inFile, outFile string, conf *model.Configuration) (err error)](#ResetPageLayoutFile)
- [func ResetPageMode(rs io.ReadSeeker, w io.Writer, conf *model.Configuration) error](#ResetPageMode)
- [func ResetPageModeFile(inFile, outFile string, conf *model.Configuration) (err error)](#ResetPageModeFile)
- [func ResetViewerPreferences(rs io.ReadSeeker, w io.Writer, conf *model.Configuration) error](#ResetViewerPreferences)
- [func ResetViewerPreferencesFile(inFile, outFile string, conf *model.Configuration) (err error)](#ResetViewerPreferencesFile)
- [func Resize(rs io.ReadSeeker, w io.Writer, selectedPages []string, resize *model.Resize, ...) error](#Resize)
- [func ResizeFile(inFile, outFile string, selectedPages []string, resize *model.Resize, ...) (err error)](#ResizeFile)
- [func Rotate(rs io.ReadSeeker, w io.Writer, rotation int, selectedPages []string, ...) error](#Rotate)
- [func RotateFile(inFile, outFile string, rotation int, selectedPages []string, ...) (err error)](#RotateFile)
- [func SetPageLayout(rs io.ReadSeeker, w io.Writer, val model.PageLayout, conf *model.Configuration) error](#SetPageLayout)
- [func SetPageLayoutFile(inFile, outFile string, val model.PageLayout, conf *model.Configuration) (err error)](#SetPageLayoutFile)
- [func SetPageMode(rs io.ReadSeeker, w io.Writer, val model.PageMode, conf *model.Configuration) error](#SetPageMode)
- [func SetPageModeFile(inFile, outFile string, val model.PageMode, conf *model.Configuration) (err error)](#SetPageModeFile)
- [func SetPermissions(rs io.ReadSeeker, w io.Writer, conf *model.Configuration) error](#SetPermissions)
- [func SetPermissionsFile(inFile, outFile string, conf *model.Configuration) (err error)](#SetPermissionsFile)
- [func SetViewerPreferences(rs io.ReadSeeker, w io.Writer, vp model.ViewerPreferences, ...) error](#SetViewerPreferences)
- [func SetViewerPreferencesFile(inFile, outFile string, vp model.ViewerPreferences, conf *model.Configuration) (err error)](#SetViewerPreferencesFile)
- [func SetViewerPreferencesFileFromJSONBytes(inFile, outFile string, jsonBytes []byte, conf *model.Configuration) (err error)](#SetViewerPreferencesFileFromJSONBytes)
- [func SetViewerPreferencesFileFromJSONFile(inFilePDF, outFilePDF, inFileJSON string, conf *model.Configuration) error](#SetViewerPreferencesFileFromJSONFile)
- [func SetViewerPreferencesFromJSONBytes(rs io.ReadSeeker, w io.Writer, jsonBytes []byte, conf *model.Configuration) error](#SetViewerPreferencesFromJSONBytes)
- [func SetViewerPreferencesFromJSONReader(rs io.ReadSeeker, w io.Writer, rd io.Reader, conf *model.Configuration) error](#SetViewerPreferencesFromJSONReader)
- [func Split(rs io.ReadSeeker, outDir, fileName string, span int, conf *model.Configuration) error](#Split)
- [func SplitByPageNr(rs io.ReadSeeker, outDir, fileName string, pageNrs []int, ...) error](#SplitByPageNr)
- [func SplitByPageNrFile(inFile, outDir string, pageNrs []int, conf *model.Configuration) error](#SplitByPageNrFile)
- [func SplitFile(inFile, outDir string, span int, conf *model.Configuration) error](#SplitFile)
- [func TextWatermark(text, desc string, onTop, update bool, u types.DisplayUnit) (*model.Watermark, error)](#TextWatermark)
- [func Trim(rs io.ReadSeeker, w io.Writer, selectedPages []string, ...) error](#Trim)
- [func TrimFile(inFile, outFile string, selectedPages []string, conf *model.Configuration) (err error)](#TrimFile)
- [func UnlockFormFields(rs io.ReadSeeker, w io.Writer, fieldIDsOrNames []string, ...) error](#UnlockFormFields)
- [func UnlockFormFieldsFile(inFile, outFile string, fieldIDsOrNames []string, conf *model.Configuration) (err error)](#UnlockFormFieldsFile)
- [func UpdateImageWatermarksFile(inFile, outFile string, selectedPages []string, onTop bool, ...) error](#UpdateImageWatermarksFile)
- [func UpdateImages(rs io.ReadSeeker, rd io.Reader, w io.Writer, objNr, pageNr int, id string, ...) error](#UpdateImages)
- [func UpdateImagesFile(inFile, imageFile, outFile string, objNr, pageNr int, id string, ...) (err error)](#UpdateImagesFile)
- [func UpdatePDFWatermarksFile(inFile, outFile string, selectedPages []string, onTop bool, ...) error](#UpdatePDFWatermarksFile)
- [func UpdateTextWatermarksFile(inFile, outFile string, selectedPages []string, onTop bool, text, desc string, ...) error](#UpdateTextWatermarksFile)
- [func Validate(rs io.ReadSeeker, conf *model.Configuration) error](#Validate)
- [func ValidateContext(ctx *model.Context) error](#ValidateContext)
- [func ValidateFile(inFile string, conf *model.Configuration) error](#ValidateFile)
- [func ValidateFiles(inFiles []string, conf *model.Configuration) error](#ValidateFiles)
- [func ValidateSignatures(inFile string, all bool, conf *model.Configuration) ([]*model.SignatureValidationResult, error)](#ValidateSignatures)
- [func ValidateSignaturesFile(inFile string, all, full bool, conf *model.Configuration) ([]string, error)](#ValidateSignaturesFile)
- [func ViewerPreferences(rs io.ReadSeeker, conf *model.Configuration) (*model.ViewerPreferences, *model.Version, error)](#ViewerPreferences)
- [func ViewerPreferencesFile(inFile string, all bool, conf *model.Configuration) (*model.ViewerPreferences, error)](#ViewerPreferencesFile)
- [func WatermarkContext(ctx *model.Context, selectedPages types.IntSet, wm *model.Watermark) error](#WatermarkContext)
- [func Write(ctx *model.Context, w io.Writer, conf *model.Configuration) error](#Write)
- [func WriteContext(ctx *model.Context, w io.Writer) error](#WriteContext)
- [func WriteContextFile(ctx *model.Context, outFile string) error](#WriteContextFile)
- [func WriteIncr(ctx *model.Context, rws io.ReadWriteSeeker, conf *model.Configuration) error](#WriteIncr)
- [func WriteIncrement(ctx *model.Context, w io.Writer) error](#WriteIncrement)
- [func WritePage(r io.Reader, outDir, fileName string, pageNr int) error](#WritePage)
- [func Zoom(rs io.ReadSeeker, w io.Writer, selectedPages []string, zoom *model.Zoom, ...) error](#Zoom)
- [func ZoomFile(inFile, outFile string, selectedPages []string, zoom *model.Zoom, ...) (err error)](#ZoomFile)
- [type PageSpan](#PageSpan)
    - [func SplitRaw(rs io.ReadSeeker, span int, conf *model.Configuration) ([]*PageSpan, error)](#SplitRaw)

#### [Examples ¶](#pkg-examples)

- [AddAttachmentsFile](#example-AddAttachmentsFile)
- [AddWatermarksFile](#example-AddWatermarksFile)
- [ChangeOwnerPasswordFile](#example-ChangeOwnerPasswordFile)
- [ChangeUserPasswordFile](#example-ChangeUserPasswordFile)
- [DecryptFile](#example-DecryptFile)
- [EncryptFile](#example-EncryptFile)
- [ExtractAttachmentsFile](#example-ExtractAttachmentsFile)
- [ExtractContentFile](#example-ExtractContentFile)
- [ExtractFontsFile](#example-ExtractFontsFile)
- [ExtractImagesFile](#example-ExtractImagesFile)
- [ExtractMetadataFile](#example-ExtractMetadataFile)
- [ExtractPagesFile](#example-ExtractPagesFile)
- [ImportImagesFile](#example-ImportImagesFile)
- [InsertPagesFile](#example-InsertPagesFile)
- [MergeAppendFile](#example-MergeAppendFile)
- [MergeCreateFile](#example-MergeCreateFile)
- [NUpFile](#example-NUpFile)
- [OptimizeFile](#example-OptimizeFile)
- [RemoveAttachmentsFile](#example-RemoveAttachmentsFile)
- [RemovePagesFile](#example-RemovePagesFile)
- [RemoveWatermarksFile](#example-RemoveWatermarksFile)
- [RotateFile](#example-RotateFile)
- [SetPermissionsFile](#example-SetPermissionsFile)
- [SplitFile](#example-SplitFile)
- [TrimFile](#example-TrimFile)
- [ValidateFile](#example-ValidateFile)

### [Constants ¶](#pkg-constants)

This section is empty.

### [Variables ¶](#pkg-variables)

[View Source](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/bookmark.go#L28)

`var ( ErrNoOutlines =` [`errors`](/github.com/pkg/errors) `.` [`New`](/github.com/pkg/errors#New) `("pdfcpu: no outlines available") ErrOutlines   =` [`errors`](/github.com/pkg/errors) `.` [`New`](/github.com/pkg/errors#New) `("pdfcpu: existing outlines") )`

[View Source](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/form.go#L38)

`var ( ErrNoFormData           =` [`errors`](/github.com/pkg/errors) `.` [`New`](/github.com/pkg/errors#New) `("pdfcpu: missing form data") ErrNoFormFieldsAffected =` [`errors`](/github.com/pkg/errors) `.` [`New`](/github.com/pkg/errors#New) `("pdfcpu: no form fields affected") ErrInvalidCSV           =` [`errors`](/github.com/pkg/errors) `.` [`New`](/github.com/pkg/errors#New) `("pdfcpu: invalid csv input file") ErrInvalidJSON          =` [`errors`](/github.com/pkg/errors) `.` [`New`](/github.com/pkg/errors#New) `("pdfcpu: invalid JSON encoding") )`

[View Source](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/viewerPreferences.go#L31)

`var ErrNoOp =` [`errors`](/github.com/pkg/errors) `.` [`New`](/github.com/pkg/errors#New) `("pdfcpu: no operation")`

### [Functions ¶](#pkg-functions)

#### [func AddAnnotations ¶ added in v0.3.12](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/annotation.go#L53)

`func AddAnnotations(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, selectedPages []` [`string`](/builtin#string) `, ann` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`AnnotationRenderer`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#AnnotationRenderer) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

AddAnnotations adds annotations for selected pages in rs and writes the result to w.

#### [func AddAnnotationsAsIncrement ¶ added in v0.3.12](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/annotation.go#L85)

`func AddAnnotationsAsIncrement(rws` [`io`](/io) `.` [`ReadWriteSeeker`](/io#ReadWriteSeeker) `, selectedPages []` [`string`](/builtin#string) `, ar` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`AnnotationRenderer`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#AnnotationRenderer) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

AddAnnotationsAsIncrement adds annotations for selected pages in rws and writes out a PDF increment.

#### [func AddAnnotationsFile ¶ added in v0.3.12](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/annotation.go#L121)

`func AddAnnotationsFile(inFile, outFile` [`string`](/builtin#string) `, selectedPages []` [`string`](/builtin#string) `, ar` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`AnnotationRenderer`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#AnnotationRenderer) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `, incr` [`bool`](/builtin#bool) `) (err` [`error`](/builtin#error) `)`

AddAnnotationsFile adds annotations for selected pages to a PDF context read from inFile and writes the result to outFile.

#### [func AddAnnotationsMap ¶ added in v0.3.12](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/annotation.go#L171)

`func AddAnnotationsMap(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, m map[` [`int`](/builtin#int) `][]` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`AnnotationRenderer`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#AnnotationRenderer) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

AddAnnotationsMap adds annotations in m to corresponding pages of rs and writes the result to w.

#### [func AddAnnotationsMapAsIncrement ¶ added in v0.3.12](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/annotation.go#L198)

`func AddAnnotationsMapAsIncrement(rws` [`io`](/io) `.` [`ReadWriteSeeker`](/io#ReadWriteSeeker) `, m map[` [`int`](/builtin#int) `][]` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`AnnotationRenderer`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#AnnotationRenderer) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

AddAnnotationsMapAsIncrement adds annotations in m to corresponding pages of rws and writes out a PDF increment.

#### [func AddAnnotationsMapFile ¶ added in v0.3.12](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/annotation.go#L229)

`func AddAnnotationsMapFile(inFile, outFile` [`string`](/builtin#string) `, m map[` [`int`](/builtin#int) `][]` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`AnnotationRenderer`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#AnnotationRenderer) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `, incr` [`bool`](/builtin#bool) `) (err` [`error`](/builtin#error) `)`

AddAnnotationsMapFile adds annotations in m to corresponding pages of inFile and writes the result to outFile.

#### [func AddAttachments ¶](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/attach.go#L51)

`func AddAttachments(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, files []` [`string`](/builtin#string) `, coll` [`bool`](/builtin#bool) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

AddAttachments embeds files into a PDF context read from rs and writes the result to w.

file is either a file name or a file name and a description separated by a comma.

#### [func AddAttachmentsFile ¶ added in v0.2.3](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/attach.go#L114)

`func AddAttachmentsFile(inFile, outFile` [`string`](/builtin#string) `, files []` [`string`](/builtin#string) `, coll` [`bool`](/builtin#bool) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

AddAttachmentsFile embeds files into a PDF context read from inFile and writes the result to outFile.

Example [¶](#example-AddAttachmentsFile)

```
// Attach 3 files to in.pdf.
AddAttachmentsFile("in.pdf", "", []string{"img.jpg", "attach.pdf", "test.zip"}, false, nil)
```

#### [func AddBookmarks ¶ added in v0.3.12](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/bookmark.go#L191)

`func AddBookmarks(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, bms []` [`pdfcpu`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu) `.` [`Bookmark`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu#Bookmark) `, replace` [`bool`](/builtin#bool) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

AddBookmarks adds a single bookmark outline layer to the PDF context read from rs and writes the result to w.

#### [func AddBookmarksFile ¶ added in v0.3.12](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/bookmark.go#L220)

`func AddBookmarksFile(inFile, outFile` [`string`](/builtin#string) `, bms []` [`pdfcpu`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu) `.` [`Bookmark`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu#Bookmark) `, replace` [`bool`](/builtin#bool) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

AddBookmarksFile adds outlines to the PDF context read from inFile and writes the result to outFile.

#### [func AddBoxes ¶ added in v0.3.8](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/box.go#L69)

`func AddBoxes(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, selectedPages []` [`string`](/builtin#string) `, pb *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`PageBoundaries`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#PageBoundaries) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

AddBoxes adds page boundaries for selected pages of rs and writes result to w.

#### [func AddBoxesFile ¶ added in v0.3.8](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/box.go#L97)

`func AddBoxesFile(inFile, outFile` [`string`](/builtin#string) `, selectedPages []` [`string`](/builtin#string) `, pb *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`PageBoundaries`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#PageBoundaries) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

AddBoxesFile adds page boundaries for selected pages of inFile and writes result to outFile.

#### [func AddImageWatermarksFile ¶ added in v0.3.4](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/stamp.go#L446)

`func AddImageWatermarksFile(inFile, outFile` [`string`](/builtin#string) `, selectedPages []` [`string`](/builtin#string) `, onTop` [`bool`](/builtin#bool) `, fileName, desc` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

AddImageWatermarksFile adds image stamps/watermarks to all selected pages of inFile and writes the result to outFile.

#### [func AddImageWatermarksForReaderFile ¶ added in v0.3.12](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/stamp.go#L461)

`func AddImageWatermarksForReaderFile(inFile, outFile` [`string`](/builtin#string) `, selectedPages []` [`string`](/builtin#string) `, onTop` [`bool`](/builtin#bool) `, r` [`io`](/io) `.` [`Reader`](/io#Reader) `, desc` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

AddImageWatermarksForReaderFile adds image stamps/watermarks to all selected pages of inFile for r and writes the result to outFile.

#### [func AddKeywords ¶ added in v0.3.2](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/keyword.go#L50)

`func AddKeywords(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, files []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

AddKeywords adds keywords to rs's infodict and writes the result to w.

#### [func AddKeywordsFile ¶ added in v0.3.2](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/keyword.go#L75)

`func AddKeywordsFile(inFile, outFile` [`string`](/builtin#string) `, files []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

AddKeywordsFile adds keywords to inFile's infodict and writes the result to outFile.

#### [func AddPDFWatermarksFile ¶ added in v0.3.4](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/stamp.go#L476)

`func AddPDFWatermarksFile(inFile, outFile` [`string`](/builtin#string) `, selectedPages []` [`string`](/builtin#string) `, onTop` [`bool`](/builtin#bool) `, fileName, desc` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

AddPDFWatermarksFile adds PDF stamps/watermarks to inFile and writes the result to outFile.

#### [func AddProperties ¶ added in v0.3.2](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/property.go#L49)

`func AddProperties(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, properties map[` [`string`](/builtin#string) `]` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

AddProperties adds properties to rs's infodict and writes the result to w.

#### [func AddPropertiesFile ¶ added in v0.3.2](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/property.go#L74)

`func AddPropertiesFile(inFile, outFile` [`string`](/builtin#string) `, properties map[` [`string`](/builtin#string) `]` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

AddPropertiesFile adds properties to inFile's infodict and writes the result to outFile.

#### [func AddTextWatermarksFile ¶ added in v0.3.4](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/stamp.go#L431)

`func AddTextWatermarksFile(inFile, outFile` [`string`](/builtin#string) `, selectedPages []` [`string`](/builtin#string) `, onTop` [`bool`](/builtin#bool) `, text, desc` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

AddTextWatermarksFile adds text stamps/watermarks to all selected pages of inFile and writes the result to outFile.

#### [func AddWatermarks ¶ added in v0.1.16](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/stamp.go#L171)

`func AddWatermarks(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, selectedPages []` [`string`](/builtin#string) `, wm *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Watermark`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Watermark) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

AddWatermarks adds watermarks to all pages selected in rs and writes the result to w.

#### [func AddWatermarksFile ¶ added in v0.2.3](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/stamp.go#L205)

`func AddWatermarksFile(inFile, outFile` [`string`](/builtin#string) `, selectedPages []` [`string`](/builtin#string) `, wm *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Watermark`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Watermark) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

AddWatermarksFile adds watermarks to all selected pages of inFile and writes the result to outFile.

Example [¶](#example-AddWatermarksFile)

```
// Unique abbreviations are accepted for all watermark descriptor parameters.
// eg. sc = scalefactor or rot = rotation

// Add a "Demo" watermark to all pages of in.pdf along the diagonal running from lower left to upper right.
onTop := false
update := false
wm, _ := TextWatermark("Demo", "", onTop, update, types.POINTS)
AddWatermarksFile("in.pdf", "", nil, wm, nil)

// Stamp all odd pages of in.pdf in red "Confidential" in 48 point Courier
// using a rotation angle of 45 degrees and an absolute scalefactor of 1.0.
onTop = true
wm, _ = TextWatermark("Confidential", "font:Courier, points:48, col: 1 0 0, rot:45, scale:1 abs, ", onTop, update, types.POINTS)
AddWatermarksFile("in.pdf", "", []string{"odd"}, wm, nil)

// Add image stamps to in.pdf using absolute scaling and a negative rotation of 90 degrees.
wm, _ = ImageWatermark("image.png", "scalefactor:.5 a, rot:-90", onTop, update, types.POINTS)
AddWatermarksFile("in.pdf", "", nil, wm, nil)

// Add a PDF stamp to all pages of in.pdf using the 2nd page of stamp.pdf, use absolute scaling of 0.5
// and rotate along the 2nd diagonal running from upper left to lower right corner.
wm, _ = PDFWatermark("stamp.pdf:2", "scale:.5 abs, diagonal:2", onTop, update, types.POINTS)
AddWatermarksFile("in.pdf", "", nil, wm, nil)
```

#### [func AddWatermarksMap ¶ added in v0.3.8](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/stamp.go#L35)

`func AddWatermarksMap(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, m map[` [`int`](/builtin#int) `]*` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Watermark`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Watermark) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

AddWatermarksMap adds watermarks in m to corresponding pages in rs and writes the result to w.

#### [func AddWatermarksMapFile ¶ added in v0.3.8](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/stamp.go#L62)

`func AddWatermarksMapFile(inFile, outFile` [`string`](/builtin#string) `, m map[` [`int`](/builtin#int) `]*` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Watermark`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Watermark) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

AddWatermarksMapFile adds watermarks to corresponding pages in m of inFile and writes the result to outFile.

#### [func AddWatermarksSliceMap ¶ added in v0.3.10](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/stamp.go#L103)

`func AddWatermarksSliceMap(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, m map[` [`int`](/builtin#int) `][]*` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Watermark`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Watermark) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

AddWatermarksSliceMap adds watermarks in m to corresponding pages in rs and writes the result to w.

#### [func AddWatermarksSliceMapFile ¶ added in v0.3.10](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/stamp.go#L130)

`func AddWatermarksSliceMapFile(inFile, outFile` [`string`](/builtin#string) `, m map[` [`int`](/builtin#int) `][]*` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Watermark`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Watermark) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

AddWatermarksSliceMapFile adds watermarks to corresponding pages in m of inFile and writes the result to outFile.

#### [func Annotations ¶ added in v0.5.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/annotation.go#L29)

`func Annotations(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, selectedPages []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (map[` [`int`](/builtin#int) `]` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`PgAnnots`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#PgAnnots) `,` [`error`](/builtin#error) `)`

Annotations returns page annotations of rs for selected pages.

#### [func Attachments ¶ added in v0.5.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/attach.go#L31)

`func Attachments(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) ([]` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Attachment`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Attachment) `,` [`error`](/builtin#error) `)`

Attachments returns rs's attachments.

#### [func Booklet ¶ added in v0.3.9](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/booklet.go#L59)

`func Booklet(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, imgFiles, selectedPages []` [`string`](/builtin#string) `, nup *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`NUp`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#NUp) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

Booklet arranges PDF pages on larger sheets of paper and writes the result to w.

#### [func BookletFile ¶ added in v0.3.9](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/booklet.go#L104)

`func BookletFile(inFiles []` [`string`](/builtin#string) `, outFile` [`string`](/builtin#string) `, selectedPages []` [`string`](/builtin#string) `, nup *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`NUp`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#NUp) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

BookletFile rearranges PDF pages or images into a booklet layout and writes the result to outFile.

#### [func BookletFromImages ¶ added in v0.3.9](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/booklet.go#L31)

`func BookletFromImages(conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `, imageFileNames []` [`string`](/builtin#string) `, nup *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`NUp`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#NUp) `) (*` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Context`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Context) `,` [`error`](/builtin#error) `)`

BookletFromImages creates a booklet from images.

#### [func Bookmarks ¶ added in v0.5.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/bookmark.go#L34)

`func Bookmarks(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) ([]` [`pdfcpu`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu) `.` [`Bookmark`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu#Bookmark) `,` [`error`](/builtin#error) `)`

Bookmarks returns rs's bookmark hierarchy.

#### [func Box ¶ added in v0.3.8](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/box.go#L40)

`func Box(s` [`string`](/builtin#string) `, u` [`types`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/types) `.` [`DisplayUnit`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/types#DisplayUnit) `) (*` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Box`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Box) `,` [`error`](/builtin#error) `)`

Box parses a box definition.

#### [func Boxes ¶ added in v0.5.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/box.go#L45)

`func Boxes(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, selectedPages []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) ([]` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`PageBoundaries`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#PageBoundaries) `,` [`error`](/builtin#error) `)`

Boxes returns rs's page boundaries for selected pages of rs.

#### [func ChangeOwnerPassword ¶](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/crypto.go#L224)

`func ChangeOwnerPassword(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, pwOld, pwNew` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

ChangeOwnerPassword reads a PDF stream from rs, changes the owner password and writes the encrypted PDF stream to w.

A configuration containing the current passwords is required.

#### [func ChangeOwnerPasswordFile ¶ added in v0.2.3](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/crypto.go#L242)

`func ChangeOwnerPasswordFile(inFile, outFile` [`string`](/builtin#string) `, pwOld, pwNew` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

ChangeOwnerPasswordFile reads inFile, changes the owner password and writes the result to outFile.

A configuration containing the current passwords is required.

Example [¶](#example-ChangeOwnerPasswordFile)

```
// Changing the owner password for an AES-256 encrypted file.
conf := model.NewAESConfiguration("upw", "opw", 256)
ChangeOwnerPasswordFile("in.pdf", "", "opw", "opwNew", conf)
```

#### [func ChangeUserPassword ¶](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/crypto.go#L155)

`func ChangeUserPassword(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, pwOld, pwNew` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

ChangeUserPassword reads a PDF stream from rs, changes the user password and writes the encrypted PDF stream to w.

A configuration containing the current passwords is required.

#### [func ChangeUserPasswordFile ¶ added in v0.2.3](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/crypto.go#L173)

`func ChangeUserPasswordFile(inFile, outFile` [`string`](/builtin#string) `, pwOld, pwNew` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

ChangeUserPasswordFile reads inFile, changes the user password and writes the result to outFile.

A configuration containing the current passwords is required.

Example [¶](#example-ChangeUserPasswordFile)

```
// Changing the user password for an AES-256 encrypted file.
conf := model.NewAESConfiguration("upw", "opw", 256)
ChangeUserPasswordFile("in.pdf", "", "upw", "upwNew", conf)
```

#### [func Collect ¶ added in v0.3.2](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/collect.go#L29)

`func Collect(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, selectedPages []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

Collect creates a custom PDF page sequence for selected pages of rs and writes the result to w.

#### [func CollectFile ¶ added in v0.3.2](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/collect.go#L58)

`func CollectFile(inFile, outFile` [`string`](/builtin#string) `, selectedPages []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

CollectFile creates a custom PDF page sequence for inFile and writes the result to outFile.

#### [func Create ¶ added in v0.4.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/create.go#L45)

`func Create(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, rd` [`io`](/io) `.` [`Reader`](/io#Reader) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

Create renders the PDF structure represented by rs into w.

If rs is present, new PDF content will be appended including any empty pages needed.

rd is a JSON representation of PDF page content which may include form data.

#### [func CreateCheatSheetsUserFonts ¶ added in v0.3.7](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/font.go#L240)

`func CreateCheatSheetsUserFonts(fontNames []` [`string`](/builtin#string) `)` [`error`](/builtin#error)

CreateCheatSheetsUserFonts creates single page PDF cheat sheets for installed user fonts.

#### [func CreateFile ¶ added in v0.4.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/create.go#L94)

`func CreateFile(inFilePDF, inFileJSON, outFilePDF` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

CreateFile renders the PDF structure represented by inFileJSON into outFilePDF.

If inFilePDF is present, new PDF content will be appended including any empty pages needed.

inFileJSON represents PDF page content which may include form data.

#### [func CreatePDFFile ¶ added in v0.2.3](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/create.go#L32)

`func CreatePDFFile(xRefTable *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`XRefTable`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#XRefTable) `, outFile` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

CreatePDFFile creates a PDF file for an xRefTable and writes it to outFile.

#### [func CreateUserFontDemoFiles ¶ added in v0.3.7](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/font.go#L208)

`func CreateUserFontDemoFiles(dir, fn` [`string`](/builtin#string) `)` [`error`](/builtin#error)

CreateUserFontDemoFiles creates single page PDF for each Unicode plane covered.

#### [func Crop ¶ added in v0.3.8](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/box.go#L216)

`func Crop(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, selectedPages []` [`string`](/builtin#string) `, b *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Box`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Box) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

Crop adds crop boxes for selected pages of rs and writes result to w.

#### [func CropFile ¶ added in v0.3.8](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/box.go#L244)

`func CropFile(inFile, outFile` [`string`](/builtin#string) `, selectedPages []` [`string`](/builtin#string) `, b *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Box`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Box) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

CropFile adds crop boxes for selected pages of inFile and writes result to outFile.

#### [func Cut ¶ added in v0.4.1](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/cut.go#L215)

`func Cut(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, outDir, fileName` [`string`](/builtin#string) `, selectedPages []` [`string`](/builtin#string) `, cut *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Cut`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Cut) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

Cut applies cutConf for selected pages of rs and writes results to outDir.

#### [func CutFile ¶ added in v0.4.1](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/cut.go#L270)

`func CutFile(inFile, outDir, outFile` [`string`](/builtin#string) `, selectedPages []` [`string`](/builtin#string) `, cut *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Cut`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Cut) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

CutFile applies cutConf for selected pages of inFile and writes results to outDir.

#### [func Decrypt ¶](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/crypto.go#L92)

`func Decrypt(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

Decrypt reads a PDF stream from rs and writes the encrypted PDF stream to w.

A configuration containing at least the current passwords is required.

#### [func DecryptFile ¶ added in v0.2.3](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/crypto.go#L107)

`func DecryptFile(inFile, outFile` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

DecryptFile decrypts inFile and writes the result to outFile.

A configuration containing at least the current passwords is required.

Example [¶](#example-DecryptFile)

```
// Decrypting an AES-256 encrypted file.
conf := model.NewAESConfiguration("upw", "opw", 256)
DecryptFile("in.pdf", "", conf)
```

#### [func DisableConfigDir ¶ added in v0.3.6](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/api.go#L257)

```
func DisableConfigDir()
```

DisableConfigDir disables the configuration directory.

Any needed default configuration will be loaded from configuration.go

Since the config dir also contains the user font dir, this also limits font usage to the default core font set

No user fonts will be available.

#### [func DumpObject ¶ added in v0.4.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/validate.go#L132)

`func DumpObject(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, mode, objNr` [`int`](/builtin#int) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

DumpObject writes an object from rs to stdout.

#### [func DumpObjectFile ¶ added in v0.4.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/validate.go#L161)

`func DumpObjectFile(inFile` [`string`](/builtin#string) `, mode, objNr` [`int`](/builtin#int) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

DumpObjectFile writes an object from rs to stdout.

#### [func Encrypt ¶](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/crypto.go#L29)

`func Encrypt(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

Encrypt reads a PDF stream from rs and writes the encrypted PDF stream to w.

A configuration containing at least the current passwords is required.

#### [func EncryptFile ¶ added in v0.2.3](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/crypto.go#L44)

`func EncryptFile(inFile, outFile` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

EncryptFile encrypts inFile and writes the result to outFile.

A configuration containing at least the current passwords is required.

Example [¶](#example-EncryptFile)

```
// Encrypting a file using AES-256.
conf := model.NewAESConfiguration("upw", "opw", 256)
EncryptFile("in.pdf", "", conf)
```

#### [func EnsureDefaultConfigAt ¶ added in v0.3.6](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/api.go#L242)

`func EnsureDefaultConfigAt(path` [`string`](/builtin#string) `)` [`error`](/builtin#error)

EnsureDefaultConfigAt switches to the pdfcpu config dir located at path.

If path/pdfcpu is not existent, it will be created including config.yml

#### [func ExportBookmarksFile ¶ added in v0.5.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/bookmark.go#L85)

`func ExportBookmarksFile(inFilePDF, outFileJSON` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

ExportBookmarksFile extracts outline data from inFilePDF and writes the result to outFileJSON.

#### [func ExportBookmarksJSON ¶ added in v0.5.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/bookmark.go#L54)

`func ExportBookmarksJSON(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, source` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

ExportBookmarksJSON extracts outline data from rs (originating from source) and writes the result to w.

#### [func ExportForm ¶ added in v0.4.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/form.go#L335)

`func ExportForm(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, source` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (*` [`form`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/form) `.` [`FormGroup`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/form#FormGroup) `,` [`error`](/builtin#error) `)`

ExportForm extracts form data originating from source from rs.

#### [func ExportFormFile ¶ added in v0.4.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/form.go#L393)

`func ExportFormFile(inFilePDF, outFileJSON` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

ExportFormFile extracts form data from inFilePDF and writes the result to outFileJSON.

#### [func ExportFormJSON ¶ added in v0.5.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/form.go#L362)

`func ExportFormJSON(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, source` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

ExportFormJSON extracts form data originating from source from rs and writes the result to w.

#### [func ExtractAttachments ¶](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/attach.go#L240)

`func ExtractAttachments(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, outDir` [`string`](/builtin#string) `, fileNames []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

ExtractAttachments extracts embedded files from a PDF context read from rs into outDir.

#### [func ExtractAttachmentsFile ¶ added in v0.2.3](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/attach.go#L269)

`func ExtractAttachmentsFile(inFile, outDir` [`string`](/builtin#string) `, files []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

ExtractAttachmentsFile extracts embedded files from a PDF context read from inFile into outDir.

Example [¶](#example-ExtractAttachmentsFile)

```
// Extract 1 attachment from in.pdf into outDir.
ExtractAttachmentsFile("in.pdf", "outDir", []string{"img.jpg"}, nil)

// Extract all attachments from in.pdf into outDir
ExtractAttachmentsFile("in.pdf", "outDir", nil, nil)
```

#### [func ExtractAttachmentsRaw ¶ added in v0.3.12](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/attach.go#L221)

`func ExtractAttachmentsRaw(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, outDir` [`string`](/builtin#string) `, fileNames []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) ([]` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Attachment`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Attachment) `,` [`error`](/builtin#error) `)`

ExtractAttachmentsRaw extracts embedded files from a PDF context read from rs.

#### [func ExtractContent ¶](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/extract.go#L305)

`func ExtractContent(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, outDir, fileName` [`string`](/builtin#string) `, selectedPages []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

ExtractContent dumps "PDF source" files from rs into outDir for selected pages.

#### [func ExtractContentFile ¶ added in v0.2.3](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/extract.go#L360)

`func ExtractContentFile(inFile, outDir` [`string`](/builtin#string) `, selectedPages []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

ExtractContentFile dumps "PDF source" files from inFile into outDir for selected pages.

Example [¶](#example-ExtractContentFile)

```
// Extract content for all pages in PDF syntax from in.pdf into outDir.
ExtractContentFile("in.pdf", "outDir", nil, nil)
```

#### [func ExtractFonts ¶](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/extract.go#L157)

`func ExtractFonts(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, outDir, fileName` [`string`](/builtin#string) `, selectedPages []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

ExtractFonts dumps embedded fontfiles from rs into outDir for selected pages.

#### [func ExtractFontsFile ¶ added in v0.2.3](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/extract.go#L203)

`func ExtractFontsFile(inFile, outDir` [`string`](/builtin#string) `, selectedPages []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

ExtractFontsFile dumps embedded fontfiles from inFile into outDir for selected pages.

Example [¶](#example-ExtractFontsFile)

```
// Extract embedded fonts for pages 1-3 from in.pdf into outDir.
ExtractFontsFile("in.pdf", "outDir", []string{"1-3"}, nil)
```

#### [func ExtractImages ¶](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/extract.go#L74)

`func ExtractImages(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, selectedPages []` [`string`](/builtin#string) `, digestImage func(` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Image`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Image) `,` [`bool`](/builtin#bool) `,` [`int`](/builtin#int) `)` [`error`](/builtin#error) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

ExtractImages extracts and digests embedded image resources from rs for selected pages.

#### [func ExtractImagesFile ¶ added in v0.2.3](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/extract.go#L122)

`func ExtractImagesFile(inFile, outDir` [`string`](/builtin#string) `, selectedPages []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

ExtractImagesFile dumps embedded image resources from inFile into outDir for selected pages.

Example [¶](#example-ExtractImagesFile)

```
// Extract embedded images from in.pdf into outDir.
ExtractImagesFile("in.pdf", "outDir", nil, nil)
```

#### [func ExtractImagesRaw ¶ added in v0.3.12](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/extract.go#L38)

`func ExtractImagesRaw(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, selectedPages []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) ([]map[` [`int`](/builtin#int) `]` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Image`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Image) `,` [`error`](/builtin#error) `)`

ExtractImagesRaw returns []pdfcpu.Image containing io.Readers for images contained in selectedPages.

Beware of memory intensive returned slice.

#### [func ExtractMetadata ¶ added in v0.1.16](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/extract.go#L375)

`func ExtractMetadata(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, outDir, fileName` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

ExtractMetadata dumps all metadata dict entries for rs into outDir.

#### [func ExtractMetadataFile ¶ added in v0.2.3](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/extract.go#L417)

`func ExtractMetadataFile(inFile, outDir` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

ExtractMetadataFile dumps all metadata dict entries for inFile into outDir.

Example [¶](#example-ExtractMetadataFile)

```
// Extract all metadata from in.pdf into outDir.
ExtractMetadataFile("in.pdf", "outDir", nil)
```

#### [func ExtractPage ¶ added in v0.8.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/extract.go#L232)

`func ExtractPage(ctx *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Context`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Context) `, pageNr` [`int`](/builtin#int) `) (` [`io`](/io) `.` [`Reader`](/io#Reader) `,` [`error`](/builtin#error) `)`

ExtractPage extracts the page with pageNr out of ctx into an io.Reader.

#### [func ExtractPages ¶](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/extract.go#L247)

`func ExtractPages(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, outDir, fileName` [`string`](/builtin#string) `, selectedPages []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

ExtractPages generates single page PDF files from rs in outDir for selected pages.

#### [func ExtractPagesFile ¶ added in v0.2.3](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/extract.go#L290)

`func ExtractPagesFile(inFile, outDir` [`string`](/builtin#string) `, selectedPages []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

ExtractPagesFile generates single page PDF files from inFile in outDir for selected pages.

Example [¶](#example-ExtractPagesFile)

```
// Extract all even numbered pages from in.pdf into outDir.
ExtractPagesFile("in.pdf", "outDir", []string{"even"}, nil)
```

#### [func FillForm ¶ added in v0.4.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/form.go#L504)

`func FillForm(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, rd` [`io`](/io) `.` [`Reader`](/io#Reader) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

FillForm populates the form rs with data from rd and writes the result to w.

#### [func FillFormFile ¶ added in v0.4.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/form.go#L573)

`func FillFormFile(inFilePDF, inFileJSON, outFilePDF` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

FillFormFile populates the form inFilePDF with data from inFileJSON and writes the result to outFilePDF.

#### [func FormFields ¶ added in v0.5.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/form.go#L46)

`func FormFields(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) ([]` [`form`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/form) `.` [`Field`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/form#Field) `,` [`error`](/builtin#error) `)`

FormFields returns all form fields of rs.

#### [func GetPermissions ¶ added in v0.3.4](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/permission.go#L119)

`func GetPermissions(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (*` [`int16`](/builtin#int16) `,` [`error`](/builtin#error) `)`

GetPermissions returns the permissions for rs.

#### [func GetPermissionsFile ¶ added in v0.3.4](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/permission.go#L144)

`func GetPermissionsFile(inFile` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (*` [`int16`](/builtin#int16) `,` [`error`](/builtin#error) `)`

GetPermissionsFile returns the permissions for inFile.

#### [func HasWatermarks ¶ added in v0.3.1](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/stamp.go#L315)

`func HasWatermarks(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (` [`bool`](/builtin#bool) `,` [`error`](/builtin#error) `)`

HasWatermarks checks rs for watermarks.

#### [func HasWatermarksFile ¶ added in v0.3.1](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/stamp.go#L333)

`func HasWatermarksFile(inFile` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (` [`bool`](/builtin#bool) `,` [`error`](/builtin#error) `)`

HasWatermarksFile checks inFile for watermarks.

#### [func ImageBookletConfig ¶ added in v0.3.9](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/nup.go#L55)

`func ImageBookletConfig(val` [`int`](/builtin#int) `, desc` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (*` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`NUp`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#NUp) `,` [`error`](/builtin#error) `)`

ImageBookletConfig returns an NUp configuration for Booklet-ing image files.

#### [func ImageGridConfig ¶ added in v0.3.9](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/nup.go#L45)

`func ImageGridConfig(rows, cols` [`int`](/builtin#int) `, desc` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (*` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`NUp`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#NUp) `,` [`error`](/builtin#error) `)`

ImageGridConfig returns a grid configuration for Grid-ing image files.

#### [func ImageNUpConfig ¶ added in v0.3.9](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/nup.go#L35)

`func ImageNUpConfig(val` [`int`](/builtin#int) `, desc` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (*` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`NUp`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#NUp) `,` [`error`](/builtin#error) `)`

ImageNUpConfig returns an NUp configuration for Nup-ing image files.

#### [func ImageWatermark ¶ added in v0.3.4](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/stamp.go#L361)

`func ImageWatermark(fileName, desc` [`string`](/builtin#string) `, onTop, update` [`bool`](/builtin#bool) `, u` [`types`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/types) `.` [`DisplayUnit`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/types#DisplayUnit) `) (*` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Watermark`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Watermark) `,` [`error`](/builtin#error) `)`

ImageWatermark returns an image watermark configuration.

#### [func ImageWatermarkForReader ¶ added in v0.3.12](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/stamp.go#L373)

`func ImageWatermarkForReader(r` [`io`](/io) `.` [`Reader`](/io#Reader) `, desc` [`string`](/builtin#string) `, onTop, update` [`bool`](/builtin#bool) `, u` [`types`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/types) `.` [`DisplayUnit`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/types#DisplayUnit) `) (*` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Watermark`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Watermark) `,` [`error`](/builtin#error) `)`

ImageWatermarkForReader returns an image watermark configuration for r.

#### [func Images ¶ added in v0.5.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/image.go#L32)

`func Images(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, selectedPages []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) ([]map[` [`int`](/builtin#int) `]` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Image`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Image) `,` [`error`](/builtin#error) `)`

Images returns all embedded images of rs.

#### [func Import ¶ added in v0.3.8](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/importImage.go#L31)

`func Import(s` [`string`](/builtin#string) `, u` [`types`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/types) `.` [`DisplayUnit`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/types#DisplayUnit) `) (*` [`pdfcpu`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu) `.` [`Import`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu#Import) `,` [`error`](/builtin#error) `)`

Import parses an Import command string into an internal structure.

#### [func ImportBookmarks ¶ added in v0.5.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/bookmark.go#L116)

`func ImportBookmarks(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, rd` [`io`](/io) `.` [`Reader`](/io#Reader) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, replace` [`bool`](/builtin#bool) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

ImportBookmarks creates/replaces outlines in rs and writes the result to w.

#### [func ImportBookmarksFile ¶ added in v0.5.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/bookmark.go#L149)

`func ImportBookmarksFile(inFilePDF, inFileJSON, outFilePDF` [`string`](/builtin#string) `, replace` [`bool`](/builtin#bool) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

ImportBookmarks creates/replaces outlines in inFilePDF and writes the result to outFilePDF.

#### [func ImportCertificates ¶ added in v0.10.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/certificate.go#L55)

`func ImportCertificates(inFiles []` [`string`](/builtin#string) `) ([]` [`string`](/builtin#string) `,` [`error`](/builtin#error) `)`

ImportCertificates validates and imports found certificate files to pdfcpu config dir.

#### [func ImportImages ¶ added in v0.1.20](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/importImage.go#L37)

`func ImportImages(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, imgs []` [`io`](/io) `.` [`Reader`](/io#Reader) `, imp *` [`pdfcpu`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu) `.` [`Import`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu#Import) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

ImportImages appends PDF pages containing images to rs and writes the result to w.

If rs == nil a new PDF file will be written to w.

#### [func ImportImagesFile ¶ added in v0.2.3](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/importImage.go#L130)

`func ImportImagesFile(imgFiles []` [`string`](/builtin#string) `, outFile` [`string`](/builtin#string) `, imp *` [`pdfcpu`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu) `.` [`Import`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu#Import) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

ImportImagesFile appends PDF pages containing images to outFile which will be created if necessary.

Example [¶](#example-ImportImagesFile)

```
// Convert an image into a single page of out.pdf which will be created if necessary.
// The page dimensions will match the image dimensions.
// If out.pdf already exists, append a new page.
// Use the default import configuration.
ImportImagesFile([]string{"image.png"}, "out.pdf", nil, nil)

// Import images by creating an A3 page for each image.
// Images are page centered with 1.0 relative scaling.
// Import an image as a new page of the existing out.pdf.
imp, _ := Import("form:A3, pos:c, s:1.0", types.POINTS)
ImportImagesFile([]string{"a1.png", "a2.jpg", "a3.tiff"}, "out.pdf", imp, nil)
```

#### [func InsertPages ¶ added in v0.2.3](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/page.go#L32)

`func InsertPages(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, selectedPages []` [`string`](/builtin#string) `, before` [`bool`](/builtin#bool) `, pageConf *` [`pdfcpu`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu) `.` [`PageConfiguration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu#PageConfiguration) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

InsertPages inserts a blank page before or after every page selected of rs and writes the result to w.

#### [func InsertPagesFile ¶ added in v0.2.3](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/page.go#L68)

`func InsertPagesFile(inFile, outFile` [`string`](/builtin#string) `, selectedPages []` [`string`](/builtin#string) `, before` [`bool`](/builtin#bool) `, pageConf *` [`pdfcpu`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu) `.` [`PageConfiguration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu#PageConfiguration) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

InsertPagesFile inserts a blank page before or after every inFile page selected and writes the result to w.

Example [¶](#example-InsertPagesFile)

```
// Insert a blank page into in.pdf before page #3.
InsertPagesFile("in.pdf", "", []string{"3"}, true, nil, nil)

// Insert a blank page into in.pdf after every page.
InsertPagesFile("in.pdf", "", nil, false, nil, nil)
```

#### [func InspectCertificates ¶ added in v0.11.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/certificate.go#L76)

`func InspectCertificates(inFiles []` [`string`](/builtin#string) `) ([]` [`string`](/builtin#string) `,` [`error`](/builtin#error) `)`

#### [func InstallFonts ¶ added in v0.3.1](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/font.go#L64)

`func InstallFonts(fileNames []` [`string`](/builtin#string) `)` [`error`](/builtin#error)

InstallFonts installs true type fonts for embedding.

#### [func Keywords ¶ added in v0.5.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/keyword.go#L29)

`func Keywords(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) ([]` [`string`](/builtin#string) `,` [`error`](/builtin#error) `)`

Keywords returns the keywords of rs's info dict.

#### [func ListFonts ¶ added in v0.3.1](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/font.go#L38)

`func ListFonts() ([]` [`string`](/builtin#string) `,` [`error`](/builtin#error) `)`

ListFonts returns a list of supported fonts.

#### [func ListPageLayout ¶ added in v0.6.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/pageLayout.go#L61)

`func ListPageLayout(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) ([]` [`string`](/builtin#string) `,` [`error`](/builtin#error) `)`

ListPageLayout lists rs's page layout.

#### [func ListPageLayoutFile ¶ added in v0.6.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/pageLayout.go#L86)

`func ListPageLayoutFile(inFile` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) ([]` [`string`](/builtin#string) `,` [`error`](/builtin#error) `)`

ListPageLayoutFile lists inFile's page layout.

#### [func ListPageMode ¶ added in v0.6.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/pageMode.go#L61)

`func ListPageMode(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) ([]` [`string`](/builtin#string) `,` [`error`](/builtin#error) `)`

ListPageMode lists rs's page mode.

#### [func ListPageModeFile ¶ added in v0.6.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/pageMode.go#L86)

`func ListPageModeFile(inFile` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) ([]` [`string`](/builtin#string) `,` [`error`](/builtin#error) `)`

ListPageModeFile lists inFile's page mode.

#### [func ListViewerPreferences ¶ added in v0.6.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/viewerPreferences.go#L77)

`func ListViewerPreferences(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, all` [`bool`](/builtin#bool) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) ([]` [`string`](/builtin#string) `,` [`error`](/builtin#error) `)`

ListViewerPreferences returns rs's viewer preferences.

#### [func ListViewerPreferencesFile ¶ added in v0.6.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/viewerPreferences.go#L150)

`func ListViewerPreferencesFile(inFile` [`string`](/builtin#string) `, all, json` [`bool`](/builtin#bool) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) ([]` [`string`](/builtin#string) `,` [`error`](/builtin#error) `)`

ListViewerPreferencesFile lists inFile's viewer preferences.

#### [func ListViewerPreferencesFileJSON ¶ added in v0.6.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/viewerPreferences.go#L110)

`func ListViewerPreferencesFileJSON(inFile` [`string`](/builtin#string) `, all` [`bool`](/builtin#bool) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) ([]` [`string`](/builtin#string) `,` [`error`](/builtin#error) `)`

ListViewerPreferencesFile lists inFile's viewer preferences in JSON.

#### [func LoadCertificates ¶ added in v0.10.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/certificate.go#L28)

`func LoadCertificates() (` [`int`](/builtin#int) `,` [`error`](/builtin#error) `)`

#### [func LoadConfiguration ¶ added in v0.3.7](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/api.go#L267)

`func LoadConfiguration() *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration)

LoadConfiguration locates and loads the default configuration

and also loads installed user fonts.

#### [func LockFormFields ¶ added in v0.4.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/form.go#L134)

`func LockFormFields(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, fieldIDsOrNames []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

LockFormFields turns form fields in rs into read-only and writes the result to w.

#### [func LockFormFieldsFile ¶ added in v0.4.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/form.go#L161)

`func LockFormFieldsFile(inFile, outFile` [`string`](/builtin#string) `, fieldIDsOrNames []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

LockFormFieldsFile turns form fields of inFile into read-only and writes the result to outFile.

#### [func Merge ¶](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/merge.go#L120)

`func Merge(destFile` [`string`](/builtin#string) `, inFiles []` [`string`](/builtin#string) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `, dividerPage` [`bool`](/builtin#bool) `)` [`error`](/builtin#error)

Merge concatenates inFiles.

if destFile is supplied it appends the result to destfile (=MERGEAPPEND)

if no destFile supplied it writes the result to the first entry of inFiles (=MERGECREATE).

#### [func MergeAppendFile ¶ added in v0.3.3](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/merge.go#L199)

`func MergeAppendFile(inFiles []` [`string`](/builtin#string) `, outFile` [`string`](/builtin#string) `, dividerPage` [`bool`](/builtin#bool) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

MergeAppendFile appends inFiles to outFile.

Example [¶](#example-MergeAppendFile)

```
// Merge inFiles by concatenation in the order specified and write the result to out.pdf.
// If out.pdf already exists it will be preserved and serves as the beginning of the merge result.
inFiles := []string{"in1.pdf", "in2.pdf"}
MergeAppendFile(inFiles, "out.pdf", false, nil)
```

#### [func MergeCreateFile ¶ added in v0.3.3](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/merge.go#L175)

`func MergeCreateFile(inFiles []` [`string`](/builtin#string) `, outFile` [`string`](/builtin#string) `, dividerPage` [`bool`](/builtin#bool) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

MergeCreateFile merges inFiles and writes the result to outFile.

Example [¶](#example-MergeCreateFile)

```
// Merge inFiles by concatenation in the order specified and write the result to out.pdf.
// out.pdf will be overwritten.
inFiles := []string{"in1.pdf", "in2.pdf"}
MergeCreateFile(inFiles, "out.pdf", false, nil)
```

#### [func MergeCreateZip ¶ added in v0.6.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/merge.go#L241)

`func MergeCreateZip(rs1, rs2` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

MergeCreateZip zips rs1 and rs2 into w.

#### [func MergeCreateZipFile ¶ added in v0.6.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/merge.go#L293)

`func MergeCreateZipFile(inFile1, inFile2, outFile` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

MergeCreateZipFile zips inFile1 and inFile2 into outFile.

#### [func MergeRaw ¶ added in v0.4.1](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/merge.go#L47)

`func MergeRaw(rsc []` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, dividerPage` [`bool`](/builtin#bool) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

MergeRaw merges a sequence of PDF streams and writes the result to w.

#### [func MultiFillForm ¶ added in v0.4.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/form.go#L816)

`func MultiFillForm(inFilePDF` [`string`](/builtin#string) `, rd` [`io`](/io) `.` [`Reader`](/io#Reader) `, outDir, fileName` [`string`](/builtin#string) `, format` [`form`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/form) `.` [`DataFormat`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/form#DataFormat) `, merge` [`bool`](/builtin#bool) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

MultiFillForm populates multiples instances of inFilePDF's form with data from rd and writes the result to outDir.

#### [func MultiFillFormFile ¶ added in v0.4.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/form.go#L832)

`func MultiFillFormFile(inFilePDF, inFileData, outDir, outFilePDF` [`string`](/builtin#string) `, merge` [`bool`](/builtin#bool) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

MultiFillFormFile populates multiples instances of inFilePDFs form with data from inFileData and writes the result to outDir.

#### [func NDown ¶ added in v0.4.1](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/cut.go#L121)

`func NDown(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, outDir, fileName` [`string`](/builtin#string) `, selectedPages []` [`string`](/builtin#string) `, n` [`int`](/builtin#int) `, cut *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Cut`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Cut) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

NDown applies n &amp; cutConf for selected pages of rs and writes results to outDir.

#### [func NDownFile ¶ added in v0.4.1](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/cut.go#L171)

`func NDownFile(inFile, outDir, outFile` [`string`](/builtin#string) `, selectedPages []` [`string`](/builtin#string) `, n` [`int`](/builtin#int) `, cut *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Cut`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Cut) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

NDownFile applies n &amp; cutConf for selected pages of inFile and writes results to outDir.

#### [func NUp ¶ added in v0.1.21](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/nup.go#L94)

`func NUp(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, imgFiles, selectedPages []` [`string`](/builtin#string) `, nup *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`NUp`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#NUp) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

NUp rearranges PDF pages or images into page grids and writes the result to w.

Either rs or imgFiles will be used.

#### [func NUpFile ¶ added in v0.2.3](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/nup.go#L138)

`func NUpFile(inFiles []` [`string`](/builtin#string) `, outFile` [`string`](/builtin#string) `, selectedPages []` [`string`](/builtin#string) `, nup *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`NUp`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#NUp) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

NUpFile rearranges PDF pages or images into page grids and writes the result to outFile.

Example [¶](#example-NUpFile)

```
// 4-Up in.pdf and write result to out.pdf.
nup, _ := PDFNUpConfig(4, "", nil)
inFiles := []string{"in.pdf"}
NUpFile(inFiles, "out.pdf", nil, nup, nil)

// 9-Up a sequence of images using format Tabloid w/o borders and no margins.
nup, _ = ImageNUpConfig(9, "f:Tabloid, b:off, m:0", nil)
inFiles = []string{"in1.png", "in2.jpg", "in3.tiff"}
NUpFile(inFiles, "out.pdf", nil, nup, nil)

// TestGridFromPDF
nup, _ = PDFGridConfig(1, 3, "f:LegalL", nil)
inFiles = []string{"in.pdf"}
NUpFile(inFiles, "out.pdf", nil, nup, nil)

// TestGridFromImages
nup, _ = ImageGridConfig(4, 2, "d:500 500, m:20, b:off", nil)
inFiles = []string{"in1.png", "in2.jpg", "in3.tiff"}
NUpFile(inFiles, "out.pdf", nil, nup, nil)
```

#### [func NUpFromImage ¶ added in v0.3.8](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/nup.go#L61)

`func NUpFromImage(conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `, imageFileNames []` [`string`](/builtin#string) `, nup *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`NUp`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#NUp) `) (*` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Context`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Context) `,` [`error`](/builtin#error) `)`

NUpFromImage creates a single page n-up PDF for one image

or a sequence of n-up pages for more than one image.

#### [func Optimize ¶](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/optimize.go#L30)

`func Optimize(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

Optimize reads a PDF stream from rs and writes the optimized PDF stream to w.

#### [func OptimizeContext ¶ added in v0.1.18](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/api.go#L114)

`func OptimizeContext(ctx *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Context`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Context) `)` [`error`](/builtin#error)

OptimizeContext optimizes ctx.

#### [func OptimizeFile ¶ added in v0.2.3](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/optimize.go#L66)

`func OptimizeFile(inFile, outFile` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

OptimizeFile reads inFile and writes the optimized PDF to outFile.

If outFile is not provided then inFile gets overwritten

which leads to the same result as when inFile equals outFile.

Example [¶](#example-OptimizeFile)

```
conf := model.NewDefaultConfiguration()

// Set passwords for encrypted files.
conf.UserPW = "upw"
conf.OwnerPW = "opw"

// Configure end of line sequence for writing.
conf.Eol = types.EolLF

// Create an optimized version of in.pdf and write it to out.pdf.
OptimizeFile("in.pdf", "out.pdf", conf)

// Create an optimized version of inFile.
// If you want to modify the original file, pass an empty string for outFile.
// Use nil for a default configuration.
OptimizeFile("in.pdf", "", nil)
```

#### [func PDFBookletConfig ¶ added in v0.3.9](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/nup.go#L50)

`func PDFBookletConfig(val` [`int`](/builtin#int) `, desc` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (*` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`NUp`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#NUp) `,` [`error`](/builtin#error) `)`

PDFBookletConfig returns an NUp configuration for Booklet-ing PDF files.

#### [func PDFGridConfig ¶ added in v0.3.9](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/nup.go#L40)

`func PDFGridConfig(rows, cols` [`int`](/builtin#int) `, desc` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (*` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`NUp`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#NUp) `,` [`error`](/builtin#error) `)`

PDFGridConfig returns a grid configuration for Grid-ing PDF files.

#### [func PDFInfo ¶ added in v0.5.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/info.go#L28)

`func PDFInfo(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, fileName` [`string`](/builtin#string) `, selectedPages []` [`string`](/builtin#string) `, fonts` [`bool`](/builtin#bool) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (*` [`pdfcpu`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu) `.` [`PDFInfo`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu#PDFInfo) `,` [`error`](/builtin#error) `)`

PDFInfo returns information about rs.

#### [func PDFMultiWatermarkForReadSeeker ¶ added in v0.6.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/stamp.go#L416)

`func PDFMultiWatermarkForReadSeeker(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, startPageNrSrc, startPageNrDest` [`int`](/builtin#int) `, desc` [`string`](/builtin#string) `, onTop, update` [`bool`](/builtin#bool) `, u` [`types`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/types) `.` [`DisplayUnit`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/types#DisplayUnit) `) (*` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Watermark`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Watermark) `,` [`error`](/builtin#error) `)`

PDFMultiWatermarkForReadSeeker returns a PDF watermark configuration.

Define a source PDF watermark/stamp sequence using rs from page startPageNrSrc thru the last page of rs.

Apply this sequence to the destination PDF file starting at page startPageNrDest for selected pages.

#### [func PDFNUpConfig ¶ added in v0.3.9](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/nup.go#L30)

`func PDFNUpConfig(val` [`int`](/builtin#int) `, desc` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (*` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`NUp`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#NUp) `,` [`error`](/builtin#error) `)`

PDFNUpConfig returns an NUp configuration for Nup-ing PDF files.

#### [func PDFWatermark ¶ added in v0.3.4](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/stamp.go#L386)

`func PDFWatermark(fileName, desc` [`string`](/builtin#string) `, onTop, update` [`bool`](/builtin#bool) `, u` [`types`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/types) `.` [`DisplayUnit`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/types#DisplayUnit) `) (*` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Watermark`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Watermark) `,` [`error`](/builtin#error) `)`

PDFWatermark returns a PDF watermark configuration.

#### [func PDFWatermarkForReadSeeker ¶ added in v0.6.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/stamp.go#L400)

`func PDFWatermarkForReadSeeker(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, pageNrSrc` [`int`](/builtin#int) `, desc` [`string`](/builtin#string) `, onTop, update` [`bool`](/builtin#bool) `, u` [`types`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/types) `.` [`DisplayUnit`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/types#DisplayUnit) `) (*` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Watermark`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Watermark) `,` [`error`](/builtin#error) `)`

PDFWatermarkForReadSeeker returns a PDF watermark configuration.

Apply watermark/stamp to destination file with pageNrSrc of rs for selected pages.

If pageNr == 0 apply a multi watermark/stamp applying all src pages in ascending manner to destination pages.

#### [func PageBoundaries ¶ added in v0.3.8](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/box.go#L35)

`func PageBoundaries(s` [`string`](/builtin#string) `, unit` [`types`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/types) `.` [`DisplayUnit`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/types#DisplayUnit) `) (*` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`PageBoundaries`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#PageBoundaries) `,` [`error`](/builtin#error) `)`

PageBoundaries parses a list of box definitions and assignments.

#### [func PageBoundariesFromBoxList ¶ added in v0.3.8](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/box.go#L30)

`func PageBoundariesFromBoxList(s` [`string`](/builtin#string) `) (*` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`PageBoundaries`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#PageBoundaries) `,` [`error`](/builtin#error) `)`

PageBoundariesFromBoxList parses a list of box types.

#### [func PageCount ¶ added in v0.2.3](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/page.go#L194)

`func PageCount(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (` [`int`](/builtin#int) `,` [`error`](/builtin#error) `)`

PageCount returns rs's page count.

#### [func PageCountFile ¶ added in v0.3.1](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/page.go#L208)

`func PageCountFile(inFile` [`string`](/builtin#string) `) (` [`int`](/builtin#int) `,` [`error`](/builtin#error) `)`

PageCountFile returns inFile's page count.

#### [func PageDims ¶ added in v0.2.4](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/page.go#L219)

`func PageDims(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) ([]` [`types`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/types) `.` [`Dim`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/types#Dim) `,` [`error`](/builtin#error) `)`

PageDims returns a sorted slice of mediaBox dimensions for rs.

#### [func PageDimsFile ¶ added in v0.2.5](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/page.go#L242)

`func PageDimsFile(inFile` [`string`](/builtin#string) `) ([]` [`types`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/types) `.` [`Dim`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/types#Dim) `,` [`error`](/builtin#error) `)`

PageDimsFile returns a sorted slice of mediaBox dimensions for inFile.

#### [func PageLayout ¶ added in v0.6.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/pageLayout.go#L29)

`func PageLayout(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (*` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`PageLayout`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#PageLayout) `,` [`error`](/builtin#error) `)`

PageLayout returns rs's page layout.

#### [func PageLayoutFile ¶ added in v0.6.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/pageLayout.go#L50)

`func PageLayoutFile(inFile` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (*` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`PageLayout`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#PageLayout) `,` [`error`](/builtin#error) `)`

PageLayoutFile returns inFile's page layout.

#### [func PageMode ¶ added in v0.6.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/pageMode.go#L29)

`func PageMode(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (*` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`PageMode`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#PageMode) `,` [`error`](/builtin#error) `)`

PageMode returns rs's page mode.

#### [func PageModeFile ¶ added in v0.6.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/pageMode.go#L50)

`func PageModeFile(inFile` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (*` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`PageMode`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#PageMode) `,` [`error`](/builtin#error) `)`

PageModeFile returns inFile's page mode.

#### [func PagesForPageCollection ¶ added in v0.3.2](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/selectPages.go#L678)

`func PagesForPageCollection(pageCount` [`int`](/builtin#int) `, pageSelection []` [`string`](/builtin#string) `) ([]` [`int`](/builtin#int) `,` [`error`](/builtin#error) `)`

PagesForPageCollection returns a slice of page numbers for a page collection.

Any page number in any order any number of times allowed.

#### [func PagesForPageRange ¶ added in v0.3.6](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/selectPages.go#L692)

`func PagesForPageRange(from, thru` [`int`](/builtin#int) `) []` [`int`](/builtin#int)

PagesForPageRange returns a slice of page numbers for a page range.

#### [func PagesForPageSelection ¶ added in v0.3.2](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/selectPages.go#L378)

`func PagesForPageSelection(pageCount` [`int`](/builtin#int) `, pageSelection []` [`string`](/builtin#string) `, ensureAllforNone` [`bool`](/builtin#bool) `, log` [`bool`](/builtin#bool) `) (` [`types`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/types) `.` [`IntSet`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/types#IntSet) `,` [`error`](/builtin#error) `)`

PagesForPageSelection ensures a set of page numbers for an ascending page sequence

where each page number may appear only once.

#### [func ParsePageSelection ¶](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/selectPages.go#L49)

`func ParsePageSelection(s` [`string`](/builtin#string) `) ([]` [`string`](/builtin#string) `,` [`error`](/builtin#error) `)`

ParsePageSelection ensures a correct page selection expression.

#### [func Permissions ¶ added in v0.5.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/permission.go#L28)

`func Permissions(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (` [`int`](/builtin#int) `,` [`error`](/builtin#error) `)`

Permissions returns user access permissions for rs.

#### [func Poster ¶ added in v0.4.1](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/cut.go#L49)

`func Poster(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, outDir, fileName` [`string`](/builtin#string) `, selectedPages []` [`string`](/builtin#string) `, cut *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Cut`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Cut) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

Poster applies cut for selected pages of rs and generates corresponding poster tiles in outDir.

#### [func PosterFile ¶ added in v0.4.1](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/cut.go#L104)

`func PosterFile(inFile, outDir, outFile` [`string`](/builtin#string) `, selectedPages []` [`string`](/builtin#string) `, cut *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Cut`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Cut) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

PosterFile applies cut for selected pages of inFile and generates corresponding poster tiles in outDir.

#### [func Properties ¶ added in v0.5.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/property.go#L29)

`func Properties(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (map[` [`string`](/builtin#string) `]` [`string`](/builtin#string) `,` [`error`](/builtin#error) `)`

Properties returns rs's properties as recorded in infoDict.

#### [func ReadAndValidate ¶ added in v0.7.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/api.go#L150)

`func ReadAndValidate(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (ctx *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Context`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Context) `, err` [`error`](/builtin#error) `)`

ReadAndValidate returns a model.Context of rs ready for processing.

#### [func ReadContext ¶ added in v0.1.18](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/api.go#L70)

`func ReadContext(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (*` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Context`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Context) `,` [`error`](/builtin#error) `)`

ReadContext uses an io.ReadSeeker to build an internal structure holding its cross reference table aka the Context.

#### [func ReadContextFile ¶ added in v0.2.3](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/api.go#L78)

`func ReadContextFile(inFile` [`string`](/builtin#string) `) (*` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Context`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Context) `,` [`error`](/builtin#error) `)`

ReadContextFile returns inFile's validated context.

#### [func ReadValidateAndOptimize ¶ added in v0.5.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/api.go#L174)

`func ReadValidateAndOptimize(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (ctx *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Context`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Context) `, err` [`error`](/builtin#error) `)`

ReadValidateAndOptimize returns an optimized model.Context of rs ready for processing a specific command.

conf.Cmd is expected to be configured properly.

#### [func RemainingPagesForPageRemoval ¶ added in v0.7.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/selectPages.go#L394)

`func RemainingPagesForPageRemoval(pageCount` [`int`](/builtin#int) `, pageSelection []` [`string`](/builtin#string) `, log` [`bool`](/builtin#bool) `) (` [`types`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/types) `.` [`IntSet`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/types#IntSet) `,` [`error`](/builtin#error) `)`

#### [func RemoveAnnotations ¶ added in v0.3.12](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/annotation.go#L281)

`func RemoveAnnotations(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, selectedPages, idsAndTypes []` [`string`](/builtin#string) `, objNrs []` [`int`](/builtin#int) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

RemoveAnnotations removes annotations for selected pages by id and object number

from a PDF context read from rs and writes the result to w.

#### [func RemoveAnnotationsAsIncrement ¶ added in v0.3.12](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/annotation.go#L314)

`func RemoveAnnotationsAsIncrement(rws` [`io`](/io) `.` [`ReadWriteSeeker`](/io#ReadWriteSeeker) `, selectedPages, idsAndTypes []` [`string`](/builtin#string) `, objNrs []` [`int`](/builtin#int) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

RemoveAnnotationsAsIncrement removes annotations for selected pages by ids and object number

from a PDF context read from rs and writes out a PDF increment.

#### [func RemoveAnnotationsFile ¶ added in v0.3.12](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/annotation.go#L351)

`func RemoveAnnotationsFile(inFile, outFile` [`string`](/builtin#string) `, selectedPages, idsAndTypes []` [`string`](/builtin#string) `, objNrs []` [`int`](/builtin#int) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `, incr` [`bool`](/builtin#bool) `) (err` [`error`](/builtin#error) `)`

RemoveAnnotationsFile removes annotations for selected pages by id and object number

from a PDF context read from inFile and writes the result to outFile.

#### [func RemoveAttachments ¶](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/attach.go#L152)

`func RemoveAttachments(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, files []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

RemoveAttachments deletes embedded files from a PDF context read from rs and writes the result to w.

#### [func RemoveAttachmentsFile ¶ added in v0.2.3](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/attach.go#L183)

`func RemoveAttachmentsFile(inFile, outFile` [`string`](/builtin#string) `, files []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

RemoveAttachmentsFile deletes embedded files from a PDF context read from inFile and writes the result to outFile.

Example [¶](#example-RemoveAttachmentsFile)

```
// Remove 1 attachment from in.pdf.
RemoveAttachmentsFile("in.pdf", "", []string{"img.jpg"}, nil)

// Remove all attachments from in.pdf
RemoveAttachmentsFile("in.pdf", "", nil, nil)
```

#### [func RemoveBookmarks ¶ added in v0.5.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/bookmark.go#L258)

`func RemoveBookmarks(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

RemoveBookmarks deletes outlines from rs and writes the result to w.

#### [func RemoveBookmarksFile ¶ added in v0.5.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/bookmark.go#L287)

`func RemoveBookmarksFile(inFile, outFile` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

RemoveBookmarksFile deletes outlines from inFile and writes the result to outFile.

#### [func RemoveBoxes ¶ added in v0.3.8](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/box.go#L142)

`func RemoveBoxes(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, selectedPages []` [`string`](/builtin#string) `, pb *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`PageBoundaries`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#PageBoundaries) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

RemoveBoxes removes page boundaries as specified in pb for selected pages of rs and writes result to w.

#### [func RemoveBoxesFile ¶ added in v0.3.8](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/box.go#L170)

`func RemoveBoxesFile(inFile, outFile` [`string`](/builtin#string) `, selectedPages []` [`string`](/builtin#string) `, pb *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`PageBoundaries`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#PageBoundaries) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

RemoveBoxesFile removes page boundaries as specified in pb for selected pages of inFile and writes result to outFile.

#### [func RemoveFormFields ¶ added in v0.4.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/form.go#L67)

`func RemoveFormFields(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, fieldIDsOrNames []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

RemoveFormFields deletes form fields in rs and writes the result to w.

#### [func RemoveFormFieldsFile ¶ added in v0.4.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/form.go#L94)

`func RemoveFormFieldsFile(inFile, outFile` [`string`](/builtin#string) `, fieldIDsOrNames []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

RemoveFormFieldsFile deletes form fields in inFile and writes the result to outFile.

#### [func RemoveKeywords ¶ added in v0.3.2](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/keyword.go#L113)

`func RemoveKeywords(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, keywords []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

RemoveKeywords deletes keywords from rs's infodict and writes the result to w.

#### [func RemoveKeywordsFile ¶ added in v0.3.2](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/keyword.go#L142)

`func RemoveKeywordsFile(inFile, outFile` [`string`](/builtin#string) `, keywords []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

RemoveKeywordsFile deletes keywords from inFile's infodict and writes the result to outFile.

#### [func RemovePages ¶ added in v0.2.3](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/page.go#L109)

`func RemovePages(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, selectedPages []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

RemovePages removes selected pages from rs and writes the result to w.

#### [func RemovePagesFile ¶ added in v0.2.3](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/page.go#L153)

`func RemovePagesFile(inFile, outFile` [`string`](/builtin#string) `, selectedPages []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

RemovePagesFile removes selected inFile pages and writes the result to outFile..

Example [¶](#example-RemovePagesFile)

```
// Remove pages 2 and 8 of in.pdf.
RemovePagesFile("in.pdf", "", []string{"2", "8"}, nil)

// Remove first 2 pages of in.pdf.
RemovePagesFile("in.pdf", "", []string{"-2"}, nil)

// Remove all pages >= 10 of in.pdf.
RemovePagesFile("in.pdf", "", []string{"10-"}, nil)
```

#### [func RemoveProperties ¶ added in v0.3.2](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/property.go#L112)

`func RemoveProperties(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, properties []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

RemoveProperties deletes properties from rs's infodict and writes the result to w.

#### [func RemovePropertiesFile ¶ added in v0.3.2](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/property.go#L141)

`func RemovePropertiesFile(inFile, outFile` [`string`](/builtin#string) `, properties []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

RemovePropertiesFile deletes properties from inFile's infodict and writes the result to outFile.

#### [func RemoveWatermarks ¶ added in v0.2.5](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/stamp.go#L246)

`func RemoveWatermarks(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, selectedPages []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

RemoveWatermarks removes watermarks from all pages selected in rs and writes the result to w.

#### [func RemoveWatermarksFile ¶ added in v0.2.5](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/stamp.go#L274)

`func RemoveWatermarksFile(inFile, outFile` [`string`](/builtin#string) `, selectedPages []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

RemoveWatermarksFile removes watermarks from all selected pages of inFile and writes the result to outFile.

Example [¶](#example-RemoveWatermarksFile)

```
// Add a "Demo" stamp to all pages of in.pdf along the diagonal running from lower left to upper right.
onTop := true
update := false
wm, _ := TextWatermark("Demo", "", onTop, update, types.POINTS)
AddWatermarksFile("in.pdf", "", nil, wm, nil)

// Update stamp for correction:
update = true
wm, _ = TextWatermark("Confidential", "", onTop, update, types.POINTS)
AddWatermarksFile("in.pdf", "", nil, wm, nil)

// Add another watermark on top of page 1
wm, _ = TextWatermark("Footer stamp", "c:.5 1 1, pos:bc", onTop, update, types.POINTS)
AddWatermarksFile("in.pdf", "", nil, wm, nil)

// Remove watermark on page 1
RemoveWatermarksFile("in.pdf", "", []string{"1"}, nil)

// Remove all watermarks
RemoveWatermarksFile("in.pdf", "", nil, nil)
```

#### [func ResetFormFields ¶ added in v0.4.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/form.go#L268)

`func ResetFormFields(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, fieldIDsOrNames []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

ResetFormFields resets form fields of rs and writes the result to w.

#### [func ResetFormFieldsFile ¶ added in v0.4.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/form.go#L295)

`func ResetFormFieldsFile(inFile, outFile` [`string`](/builtin#string) `, fieldIDsOrNames []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

ResetFormFieldsFile resets form fields of inFile and writes the result to outFile.

#### [func ResetPageLayout ¶ added in v0.6.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/pageLayout.go#L158)

`func ResetPageLayout(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

ResetPageLayout resets rs's page layout and writes the result to w.

#### [func ResetPageLayoutFile ¶ added in v0.6.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/pageLayout.go#L181)

`func ResetPageLayoutFile(inFile, outFile` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

ResetPageLayoutFile resets inFile's page layout and writes the result to outFile.

#### [func ResetPageMode ¶ added in v0.6.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/pageMode.go#L158)

`func ResetPageMode(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

ResetPageMode resets rs's page mode and writes the result to w.

#### [func ResetPageModeFile ¶ added in v0.6.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/pageMode.go#L181)

`func ResetPageModeFile(inFile, outFile` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

ResetPageModeFile resets inFile's page mode and writes the result to outFile.

#### [func ResetViewerPreferences ¶ added in v0.6.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/viewerPreferences.go#L339)

`func ResetViewerPreferences(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

ResetViewerPreferences resets rs's viewer preferences and writes the result to w.

#### [func ResetViewerPreferencesFile ¶ added in v0.6.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/viewerPreferences.go#L370)

`func ResetViewerPreferencesFile(inFile, outFile` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

ResetViewerPreferencesFile resets inFile's viewer preferences and writes the result to outFile.

#### [func Resize ¶ added in v0.4.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/resize.go#L30)

`func Resize(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, selectedPages []` [`string`](/builtin#string) `, resize *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Resize`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Resize) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

Resize applies resizeConf for selected pages of rs and writes result to w.

#### [func ResizeFile ¶ added in v0.4.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/resize.go#L58)

`func ResizeFile(inFile, outFile` [`string`](/builtin#string) `, selectedPages []` [`string`](/builtin#string) `, resize *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Resize`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Resize) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

ResizeFile applies resizeConf for selected pages of inFile and writes result to outFile.

#### [func Rotate ¶ added in v0.1.20](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/rotate.go#L29)

`func Rotate(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, rotation` [`int`](/builtin#int) `, selectedPages []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

Rotate rotates selected pages of rs clockwise by rotation degrees and writes the result to w.

#### [func RotateFile ¶ added in v0.2.3](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/rotate.go#L57)

`func RotateFile(inFile, outFile` [`string`](/builtin#string) `, rotation` [`int`](/builtin#int) `, selectedPages []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

RotateFile rotates selected pages of inFile clockwise by rotation degrees and writes the result to outFile.

Example [¶](#example-RotateFile)

```
// Rotate all pages of in.pdf, clockwise by 90 degrees and write the result to out.pdf.
RotateFile("in.pdf", "out.pdf", 90, nil, nil)

// Rotate the first page of in.pdf by 180 degrees.
// If you want to modify the original file, pass an empty string as outFile.
RotateFile("in.pdf", "", 180, []string{"1"}, nil)
```

#### [func SetPageLayout ¶ added in v0.6.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/pageLayout.go#L97)

`func SetPageLayout(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, val` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`PageLayout`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#PageLayout) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

SetPageLayout sets rs's page layout and writes the result to w.

#### [func SetPageLayoutFile ¶ added in v0.6.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/pageLayout.go#L120)

`func SetPageLayoutFile(inFile, outFile` [`string`](/builtin#string) `, val` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`PageLayout`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#PageLayout) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

SetPageLayoutFile sets inFile's page layout and writes the result to outFile.

#### [func SetPageMode ¶ added in v0.6.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/pageMode.go#L97)

`func SetPageMode(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, val` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`PageMode`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#PageMode) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

SetPageMode sets rs's page mode and writes the result to w.

#### [func SetPageModeFile ¶ added in v0.6.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/pageMode.go#L120)

`func SetPageModeFile(inFile, outFile` [`string`](/builtin#string) `, val` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`PageMode`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#PageMode) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

SetPageModeFile sets inFile's page mode and writes the result to outFile.

#### [func SetPermissions ¶ added in v0.2.3](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/permission.go#L54)

`func SetPermissions(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

SetPermissions sets user access permissions.

inFile has to be encrypted.

A configuration containing the current passwords is required.

#### [func SetPermissionsFile ¶ added in v0.2.3](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/permission.go#L75)

`func SetPermissionsFile(inFile, outFile` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

SetPermissionsFile sets inFile's user access permissions.

inFile has to be encrypted.

A configuration containing the current passwords is required.

Example [¶](#example-SetPermissionsFile)

```
// Setting all permissions for the AES-256 encrypted in.pdf.
conf := model.NewAESConfiguration("upw", "opw", 256)
conf.Permissions = model.PermissionsAll
SetPermissionsFile("in.pdf", "", conf)

// Restricting permissions for the AES-256 encrypted in.pdf.
conf = model.NewAESConfiguration("upw", "opw", 256)
conf.Permissions = model.PermissionsNone
SetPermissionsFile("in.pdf", "", conf)
```

#### [func SetViewerPreferences ¶ added in v0.6.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/viewerPreferences.go#L165)

`func SetViewerPreferences(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, vp` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`ViewerPreferences`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#ViewerPreferences) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

SetViewerPreferences sets rs's viewer preferences and writes the result to w.

#### [func SetViewerPreferencesFile ¶ added in v0.6.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/viewerPreferences.go#L249)

`func SetViewerPreferencesFile(inFile, outFile` [`string`](/builtin#string) `, vp` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`ViewerPreferences`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#ViewerPreferences) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

SetViewerPreferencesFile sets inFile's viewer preferences and writes the result to outFile.

#### [func SetViewerPreferencesFileFromJSONBytes ¶ added in v0.6.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/viewerPreferences.go#L287)

`func SetViewerPreferencesFileFromJSONBytes(inFile, outFile` [`string`](/builtin#string) `, jsonBytes []` [`byte`](/builtin#byte) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

SetViewerPreferencesFileFromJSONBytes sets inFile's viewer preferences corresponding to jsonBytes and writes the result to outFile.

#### [func SetViewerPreferencesFileFromJSONFile ¶ added in v0.6.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/viewerPreferences.go#L325)

`func SetViewerPreferencesFileFromJSONFile(inFilePDF, outFilePDF, inFileJSON` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

SetViewerPreferencesFileFromJSONFile sets inFile's viewer preferences corresponding to inFileJSON and writes the result to outFile.

#### [func SetViewerPreferencesFromJSONBytes ¶ added in v0.6.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/viewerPreferences.go#L204)

`func SetViewerPreferencesFromJSONBytes(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, jsonBytes []` [`byte`](/builtin#byte) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

SetViewerPreferencesFromJSONBytes sets rs's viewer preferences corresponding to jsonBytes and writes the result to w.

#### [func SetViewerPreferencesFromJSONReader ¶ added in v0.6.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/viewerPreferences.go#L227)

`func SetViewerPreferencesFromJSONReader(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, rd` [`io`](/io) `.` [`Reader`](/io#Reader) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

SetViewerPreferencesFromJSONReader sets rs's viewer preferences corresponding to rd and writes the result to w.

#### [func Split ¶](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/split.go#L246)

`func Split(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, outDir, fileName` [`string`](/builtin#string) `, span` [`int`](/builtin#int) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

Split generates a sequence of PDF files in outDir for the PDF stream read from rs obeying given split span.

If span == 1 splitting results in single page PDFs.

If span == 0 we split along given bookmarks (level 1 only).

Default span: 1

#### [func SplitByPageNr ¶ added in v0.6.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/split.go#L287)

`func SplitByPageNr(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, outDir, fileName` [`string`](/builtin#string) `, pageNrs []` [`int`](/builtin#int) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

SplitFile generates a sequence of PDF files in outDir for rs splitting along pageNrs.

#### [func SplitByPageNrFile ¶ added in v0.6.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/split.go#L301)

`func SplitByPageNrFile(inFile, outDir` [`string`](/builtin#string) `, pageNrs []` [`int`](/builtin#int) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

SplitFile generates a sequence of PDF files in outDir for inFile splitting it along pageNrs.

#### [func SplitFile ¶ added in v0.2.3](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/split.go#L266)

`func SplitFile(inFile, outDir` [`string`](/builtin#string) `, span` [`int`](/builtin#int) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

SplitFile generates a sequence of PDF files in outDir for inFile obeying given split span.

If span == 1 splitting results in single page PDFs.

If span == 0 we split along given bookmarks (level 1 only).

Default span: 1

Example [¶](#example-SplitFile)

```
// Create single page PDFs for in.pdf in outDir using the default configuration.
SplitFile("in.pdf", "outDir", 1, nil)

// Create dual page PDFs for in.pdf in outDir using the default configuration.
SplitFile("in.pdf", "outDir", 2, nil)

// Create a sequence of PDFs representing bookmark sections.
SplitFile("in.pdf", "outDir", 0, nil)
```

#### [func TextWatermark ¶ added in v0.3.4](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/stamp.go#L349)

`func TextWatermark(text, desc` [`string`](/builtin#string) `, onTop, update` [`bool`](/builtin#bool) `, u` [`types`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/types) `.` [`DisplayUnit`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/types#DisplayUnit) `) (*` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Watermark`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Watermark) `,` [`error`](/builtin#error) `)`

TextWatermark returns a text watermark configuration.

#### [func Trim ¶](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/trim.go#L32)

`func Trim(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, selectedPages []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

Trim generates a trimmed version of rs

containing all selected pages and writes the result to w.

#### [func TrimFile ¶ added in v0.2.3](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/trim.go#L83)

`func TrimFile(inFile, outFile` [`string`](/builtin#string) `, selectedPages []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

TrimFile generates a trimmed version of inFile

containing all selected pages and writes the result to outFile.

Example [¶](#example-TrimFile)

```
// Create a trimmed version of in.pdf containing odd page numbers only.
TrimFile("in.pdf", "outFile", []string{"odd"}, nil)

// Create a trimmed version of in.pdf containing the first two pages only.
// If you want to modify the original file, pass an empty string for outFile.
TrimFile("in.pdf", "", []string{"1-2"}, nil)
```

#### [func UnlockFormFields ¶ added in v0.4.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/form.go#L201)

`func UnlockFormFields(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, fieldIDsOrNames []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

UnlockFormFields makess form fields in rs writeable and writes the result to w.

#### [func UnlockFormFieldsFile ¶ added in v0.4.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/form.go#L228)

`func UnlockFormFieldsFile(inFile, outFile` [`string`](/builtin#string) `, fieldIDsOrNames []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

UnlockFormFieldsFile makes form fields of inFile writeable and writes the result to outFile.

#### [func UpdateImageWatermarksFile ¶ added in v0.3.4](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/stamp.go#L506)

`func UpdateImageWatermarksFile(inFile, outFile` [`string`](/builtin#string) `, selectedPages []` [`string`](/builtin#string) `, onTop` [`bool`](/builtin#bool) `, fileName, desc` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

UpdateImageWatermarksFile adds image stamps/watermarks to all selected pages of inFile and writes the result to outFile.

#### [func UpdateImages ¶ added in v0.9.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/image.go#L58)

`func UpdateImages(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, rd` [`io`](/io) `.` [`Reader`](/io#Reader) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, objNr, pageNr` [`int`](/builtin#int) `, id` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

UpdateImages replaces the XObject identified by objNr or (pageNr and resourceId).

#### [func UpdateImagesFile ¶ added in v0.9.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/image.go#L120)

`func UpdateImagesFile(inFile, imageFile, outFile` [`string`](/builtin#string) `, objNr, pageNr` [`int`](/builtin#int) `, id` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

UpdateImagesFile replaces the XObject identified by objNr or (pageNr and resourceId).

#### [func UpdatePDFWatermarksFile ¶ added in v0.3.4](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/stamp.go#L519)

`func UpdatePDFWatermarksFile(inFile, outFile` [`string`](/builtin#string) `, selectedPages []` [`string`](/builtin#string) `, onTop` [`bool`](/builtin#bool) `, fileName, desc` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

UpdatePDFWatermarksFile adds PDF stamps/watermarks to all selected pages of inFile and writes the result to outFile.

#### [func UpdateTextWatermarksFile ¶ added in v0.3.4](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/stamp.go#L491)

`func UpdateTextWatermarksFile(inFile, outFile` [`string`](/builtin#string) `, selectedPages []` [`string`](/builtin#string) `, onTop` [`bool`](/builtin#bool) `, text, desc` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

UpdateTextWatermarksFile adds text stamps/watermarks to all selected pages of inFile and writes the result to outFile.

#### [func Validate ¶](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/validate.go#L32)

`func Validate(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

Validate validates a PDF stream read from rs.

#### [func ValidateContext ¶ added in v0.1.18](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/api.go#L106)

`func ValidateContext(ctx *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Context`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Context) `)` [`error`](/builtin#error)

ValidateContext validates ctx.

#### [func ValidateFile ¶ added in v0.2.3](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/validate.go#L87)

`func ValidateFile(inFile` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

ValidateFile validates inFile.

Example [¶](#example-ValidateFile)

```
// Use the default configuration to validate in.pdf.
ValidateFile("in.pdf", nil)
```

#### [func ValidateFiles ¶ added in v0.3.13](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/validate.go#L111)

`func ValidateFiles(inFiles []` [`string`](/builtin#string) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

ValidateFiles validates inFiles.

#### [func ValidateSignatures ¶ added in v0.10.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/sign.go#L138)

`func ValidateSignatures(inFile` [`string`](/builtin#string) `, all` [`bool`](/builtin#bool) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) ([]*` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`SignatureValidationResult`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#SignatureValidationResult) `,` [`error`](/builtin#error) `)`

ValidateSignatures validates signatures of inFile and returns the signature validation results.

#### [func ValidateSignaturesFile ¶ added in v0.10.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/sign.go#L169)

`func ValidateSignaturesFile(inFile` [`string`](/builtin#string) `, all, full` [`bool`](/builtin#bool) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) ([]` [`string`](/builtin#string) `,` [`error`](/builtin#error) `)`

ValidateSignaturesFile validates signatures of inFile.

all: processes all signatures meaning not only the authoritative/certified signature..

full: verbose output including cert chain and problems encountered.

#### [func ViewerPreferences ¶ added in v0.6.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/viewerPreferences.go#L34)

`func ViewerPreferences(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (*` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`ViewerPreferences`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#ViewerPreferences) `, *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Version`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Version) `,` [`error`](/builtin#error) `)`

ViewerPreferences returns rs's viewer preferences.

#### [func ViewerPreferencesFile ¶ added in v0.6.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/viewerPreferences.go#L57)

`func ViewerPreferencesFile(inFile` [`string`](/builtin#string) `, all` [`bool`](/builtin#bool) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (*` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`ViewerPreferences`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#ViewerPreferences) `,` [`error`](/builtin#error) `)`

ViewerPreferences returns inFile's viewer preferences.

#### [func WatermarkContext ¶ added in v0.3.1](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/stamp.go#L30)

`func WatermarkContext(ctx *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Context`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Context) `, selectedPages` [`types`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/types) `.` [`IntSet`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/types#IntSet) `, wm *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Watermark`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Watermark) `)` [`error`](/builtin#error)

WatermarkContext applies wm for selected pages to ctx.

#### [func Write ¶](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/api.go#L207)

`func Write(ctx *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Context`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Context) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

#### [func WriteContext ¶ added in v0.1.18](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/api.go#L122)

`func WriteContext(ctx *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Context`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Context) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `)` [`error`](/builtin#error)

WriteContext writes ctx to w.

#### [func WriteContextFile ¶ added in v0.3.1](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/api.go#L140)

`func WriteContextFile(ctx *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Context`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Context) `, outFile` [`string`](/builtin#string) `)` [`error`](/builtin#error)

WriteContextFile writes ctx to outFile.

#### [func WriteIncr ¶ added in v0.7.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/api.go#L222)

`func WriteIncr(ctx *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Context`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Context) `, rws` [`io`](/io) `.` [`ReadWriteSeeker`](/io#ReadWriteSeeker) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

#### [func WriteIncrement ¶ added in v0.3.12](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/api.go#L133)

`func WriteIncrement(ctx *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Context`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Context) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `)` [`error`](/builtin#error)

WriteIncrement writes a PDF increment for ctx to w.

#### [func WritePage ¶ added in v0.8.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/extract.go#L218)

`func WritePage(r` [`io`](/io) `.` [`Reader`](/io#Reader) `, outDir, fileName` [`string`](/builtin#string) `, pageNr` [`int`](/builtin#int) `)` [`error`](/builtin#error)

WritePage consumes an io.Reader containing some PDF bytes and writes to outDir/fileName.

#### [func Zoom ¶ added in v0.7.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/zoom.go#L30)

`func Zoom(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, w` [`io`](/io) `.` [`Writer`](/io#Writer) `, selectedPages []` [`string`](/builtin#string) `, zoom *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Zoom`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Zoom) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `)` [`error`](/builtin#error)

Zoom applies resizeConf for selected pages of rs and writes result to w.

#### [func ZoomFile ¶ added in v0.7.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/zoom.go#L58)

`func ZoomFile(inFile, outFile` [`string`](/builtin#string) `, selectedPages []` [`string`](/builtin#string) `, zoom *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Zoom`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Zoom) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) (err` [`error`](/builtin#error) `)`

ZoomFile applies zoomConf for selected pages of inFile and writes result to outFile.

### [Types ¶](#pkg-types)

#### [type PageSpan ¶ added in v0.4.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/split.go#L33)

`type PageSpan struct { From` [`int`](/builtin#int) `Thru` [`int`](/builtin#int) `Reader` [`io`](/io) `.` [`Reader`](/io#Reader) `}`

#### [func SplitRaw ¶ added in v0.4.0](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/split.go#L226)

`func SplitRaw(rs` [`io`](/io) `.` [`ReadSeeker`](/io#ReadSeeker) `, span` [`int`](/builtin#int) `, conf *` [`model`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model) `.` [`Configuration`](/github.com/pdfcpu/pdfcpu@v0.11.0/pkg/pdfcpu/model#Configuration) `) ([]*` [`PageSpan`](#PageSpan) `,` [`error`](/builtin#error) `)`

SplitRaw returns page spans for the PDF stream read from rs obeying given split span.

If span == 1 splitting results in single page PDFs.

If span == 0 we split along given bookmarks (level 1 only).

Default span: 1

## [Source Files ¶](#section-sourcefiles)

<!-- image -->

[View all Source files](https://github.com/pdfcpu/pdfcpu/tree/v0.11.0/pkg/api)

- [annotation.go](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/annotation.go)
- [api.go](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/api.go)
- [attach.go](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/attach.go)
- [booklet.go](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/booklet.go)
- [bookmark.go](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/bookmark.go)
- [box.go](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/box.go)
- [certificate.go](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/certificate.go)
- [collect.go](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/collect.go)
- [create.go](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/create.go)
- [crypto.go](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/crypto.go)
- [cut.go](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/cut.go)
- [extract.go](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/extract.go)
- [font.go](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/font.go)
- [form.go](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/form.go)
- [image.go](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/image.go)
- [importImage.go](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/importImage.go)
- [info.go](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/info.go)
- [keyword.go](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/keyword.go)
- [merge.go](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/merge.go)
- [nup.go](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/nup.go)
- [optimize.go](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/optimize.go)
- [page.go](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/page.go)
- [pageLayout.go](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/pageLayout.go)
- [pageMode.go](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/pageMode.go)
- [permission.go](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/permission.go)
- [property.go](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/property.go)
- [resize.go](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/resize.go)
- [rotate.go](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/rotate.go)
- [selectPages.go](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/selectPages.go)
- [sign.go](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/sign.go)
- [split.go](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/split.go)
- [stamp.go](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/stamp.go)
- [trim.go](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/trim.go)
- [validate.go](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/validate.go)
- [viewerPreferences.go](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/viewerPreferences.go)
- [zoom.go](https://github.com/pdfcpu/pdfcpu/blob/v0.11.0/pkg/api/zoom.go)

Click to show internal directories.

Click to hide internal directories.

## Jump to

Close

## Keyboard shortcuts

| ?      | : This menu     |
|--------|-----------------|
| /      | : Search site   |
| f or F | : Jump to       |
| y or Y | : Canonical URL |

Close

go.dev uses cookies from Google to deliver and enhance the quality of its services and to

analyze traffic.

[Learn more.](https://policies.google.com/technologies/cookies)

Okay

--------------------------------------------------------------------------------

