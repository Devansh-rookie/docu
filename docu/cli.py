"""Command line interface for docu."""
import sys
import argparse
from typing import List, Optional
from .docgen import process_file

def parse_args(args: Optional[List[str]] = None) -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Generate documentation from Python files'
    )
    
    parser.add_argument(
        'file_path',
        help='Path to the Python file to document'
    )
    
    parser.add_argument(
        '--format', '-f',
        choices=['markdown', 'html'],
        default='html',
        help='Output format for the documentation'
    )
    
    parser.add_argument(
        '--output-dir', '-o',
        help='Directory to save the generated documentation'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose output'
    )

    parser.add_argument(
        '--template', '-t',
        default='default',
        help='HTML template name to use (only applies to HTML output)'
    )

    parser.add_argument(
        '--doc-style', '-s',
        choices=['google', 'numpy', 'sphinx'],
        default='google',
        help='Documentation style to parse'
    )
    
    return parser.parse_args(args)

def main(args: Optional[List[str]] = None) -> int:
    """Main entry point for the CLI.
    
    Args:
        args: Command line arguments (uses sys.argv if None)
        
    Returns:
        Exit code (0 for success, non-zero for error)
    """
    parsed_args = parse_args(args)
    
    try:
        output = process_file(
            parsed_args.file_path,
            output_format=parsed_args.format,
            output_dir=parsed_args.output_dir,
            template_name=parsed_args.template,
            doc_style=parsed_args.doc_style
        )
        
        if parsed_args.verbose:
            if parsed_args.output_dir:
                print(f"Documentation saved to: {output}")
            else:
                print(output)
                
        return 0
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        if parsed_args.verbose:
            raise
        return 1

if __name__ == '__main__':
    sys.exit(main())